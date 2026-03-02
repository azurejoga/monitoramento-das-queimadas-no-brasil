# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2ceeeb0-09b7-3e41-a79a-0f5106965a36 | 3.42284 | -60.83417 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d9fa6d35-ec2a-3d3b-a53d-18b6c73f3015 | 1.50428 | -59.91281 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e94efadb-3983-3c26-808b-55f1aa66e954 | 1.50818 | -59.93665 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f25a05da-ead4-3d91-aec1-de5039d6a9aa | 1.48072 | -59.929 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a706fb8-4cb6-3628-9f27-70906b5ef527 | 1.4955 | -59.92322 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d98df4bf-c275-36d6-bd49-3beaea7a95d1 | 2.86407 | -60.84083 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e70b4ac9-4838-3830-a8db-0f4b6a16bf3f | 1.08878 | -59.24718 | 2026-03-02 05:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c2bf09e-b094-33ae-bfe7-a71aff54739c | 3.45756 | -60.78315 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff3e2db4-7619-3ec6-bb58-c9feb973b51a | 1.51087 | -59.92103 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| bfee0b5e-4658-3fec-8097-dcf1e6dd3088 | 2.85 | -60.84311 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2a1bde32-b7e3-3048-a3f3-1692134ddac7 | 4.25687 | -59.89155 | 2026-03-02 05:59:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 370289c0-a86b-3179-8e8e-de0c682a7b54 | 1.87892 | -60.91133 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e42a1d46-eed1-3606-a513-df5b71ae15c9 | 3.42204 | -60.82927 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01e7589c-41f3-3638-935d-81087480ad8f | 1.47702 | -59.9249 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e9ddf30-83b3-347b-8304-b9be6ead5243 | 4.37113 | -60.62559 | 2026-03-02 05:59:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 118c1033-5e52-3925-b766-d49603312115 | 1.07373 | -59.25654 | 2026-03-02 05:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9042e6c2-b153-3219-a4ff-1a5e08599380 | 3.01344 | -60.70018 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c973183b-7f66-3f56-ba84-bbee447b2545 | 1.51039 | -59.91812 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 115d773a-58ba-359d-9f1d-20ae73f53ba7 | 1.86669 | -60.39613 | 2026-03-02 05:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bb2acda-dac0-3a7d-b69f-1a9ee7dfad09 | 1.516 | -59.92039 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e14a8627-81b7-32b6-81a8-d43330cbd465 | 3.16922 | -60.69452 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 71f394de-44a9-3329-8571-b8087b2634ae | 1.07317 | -59.25311 | 2026-03-02 05:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 499b1c05-ea70-380b-b270-1e196068a5ba | 3.46001 | -60.78192 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9412c352-628c-33fc-bdde-41bc3683737e | 2.50303 | -59.92854 | 2026-03-02 05:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7daf21b4-778d-3820-9234-a778a40b3a99 | 3.96039 | -60.87265 | 2026-03-02 05:59:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc16d9c6-0010-3848-8dad-6ca981f5574c | 1.48733 | -59.93723 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b896fec-db1a-3fe2-90ed-0b83ead0485d | 3.39826 | -59.84034 | 2026-03-02 05:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1eb696fb-c728-3098-ad08-ccaf0c34f871 | 3.39795 | -59.84231 | 2026-03-02 05:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e70eb3e-0ce3-3c98-a08f-283fa4bee20b | 3.17293 | -59.91056 | 2026-03-02 05:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0004ea56-d932-307e-babc-1cb40e875ec8 | 1.48022 | -59.92595 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2946953f-9098-3d60-82da-f6431945f4be | 3.01174 | -60.69718 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2747cfe0-e65c-3e5b-8f70-9ad06fb1f43a | 1.51135 | -59.92397 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb10afd9-3c44-396e-8a85-4118929712f9 | 1.11938 | -59.19672 | 2026-03-02 05:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55125561-9080-3182-af02-2e78521212ea | 2.8602 | -60.84656 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a8b8ee18-fc70-32b4-93c0-4120f1b80c07 | 3.419 | -60.83984 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5501d8c5-dd3f-3664-831c-2f610f7f3550 | 1.17282 | -60.82376 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad7312ad-9e64-340d-ad67-697366d3c717 | 1.51375 | -59.93868 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19cfc39b-1bfa-354d-893a-a9a5eb9e9421 | 1.8627 | -60.40245 | 2026-03-02 05:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 994aeddd-6c7b-300e-859c-6185a8a021a1 | 1.47187 | -59.92548 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ee0c64d-32f7-35b8-bf13-3f2b23aa206c | 1.45378 | -60.07328 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef43f86c-204a-3122-b5b6-de0705ade101 | 2.86325 | -60.83587 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f439bafe-1f2b-3693-a42b-02094170afab | 1.51647 | -59.92324 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fcac951-0859-306d-84c7-130c96c06869 | 3.00871 | -60.70095 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2666d9ad-809d-3a3a-b251-11078e33144d | 3.6117 | -61.6554 | 2026-03-02 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27d76596-e4e2-3efd-bfff-afa365b41959 | 3.42588 | -60.82358 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5995344f-3548-3b3d-8646-afc89797fc7d | 1.10137 | -60.18095 | 2026-03-02 05:59:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3dd8e3f-254c-32e0-904a-2b24ca1d50d5 | 1.47508 | -59.92658 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78849371-55d1-32d5-95aa-a7253a8e72fb | 3.16749 | -59.90856 | 2026-03-02 05:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b76038c-e736-3695-9837-01c21b2d1b4e | 1.47559 | -59.92964 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8829e6cf-5ecf-370f-877c-bc05a92f57b9 | 3.6462 | -61.04803 | 2026-03-02 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0bf7eb78-6572-3c8d-a7fe-914f84421169 | 4.25787 | -59.89731 | 2026-03-02 05:59:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b29a50a-3ee4-3476-a5c1-f42ea667204e | 1.50012 | -59.91942 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 463a99e7-c987-3a98-af96-c35d15ad3c72 | 1.4904 | -59.92411 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc0acef8-4708-34fc-a8b5-aacd8fdc4e76 | 3.46631 | -60.79091 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6de339cd-155d-38fa-b688-186168601fac | 1.50525 | -59.91873 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f05abdc6-2fcf-31cb-b469-d0e413ec2121 | 1.49242 | -59.93635 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 242cde2e-d318-3af5-a4ce-c94b859e4976 | 2.22527 | -60.7496 | 2026-03-02 05:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e4219b9-d183-34dd-b5da-b1b38c729861 | 1.48839 | -59.91193 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 08a2d8e9-6334-3f30-86e8-33aec93ce8d4 | 1.48582 | -59.92812 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 744babf1-550a-3465-adfa-ec99a0ffd9c9 | 3.17391 | -60.69358 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2278bfa6-dcb5-36a0-8341-bd4880cb553b | 4.37495 | -60.61985 | 2026-03-02 05:59:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 117bdc16-feef-34a7-b265-8a30bd9fbe11 | 2.86162 | -60.82594 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f0618fca-1200-344f-b137-60a02fccbf20 | 3.41274 | -60.83085 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9336fa3c-db9b-38a8-8b54-8170ad1822c5 | 1.06779 | -59.25395 | 2026-03-02 05:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17c3ca0c-c633-3d9d-a36a-235a7ac4ae94 | 1.47751 | -59.92798 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb83ad9b-b916-362b-905f-ec436a2c2cac | 1.49401 | -59.91417 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bd996947-6327-3ba0-9adc-ee842edc57ec | 1.5123 | -59.92981 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8ba8563-9cb2-38e8-ae7f-47b4981bc9bc | 1.50165 | -59.92876 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93bba776-99ac-3872-9f35-bff324839d80 | 3.1732 | -60.6893 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00890fe3-05c4-31ec-9866-8ab3cf5d8b79 | 3.01816 | -60.69941 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7361f6c2-2540-3a04-a768-950a92dbdead | 1.50476 | -59.91577 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1dc45730-63de-321b-ac37-3a85dfc536f2 | 3.16796 | -59.9114 | 2026-03-02 05:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 05180b52-d598-3e36-b0f9-2dbdcc04fd68 | 1.45835 | -60.06942 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e38205f-c7b5-33ca-8dec-735e469a22f0 | 2.67772 | -60.42467 | 2026-03-02 05:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9a81001-dc0a-3d09-ad4f-dba67229bcf2 | 1.45329 | -60.07025 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17d6cb06-1100-3b6c-97b6-a8877e441616 | 2.85224 | -60.82748 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b51aec45-98f0-330e-a196-1f1f2045554c | 2.84754 | -60.82828 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e004312d-1212-333f-90c9-392eef49d39b | 1.48888 | -59.91492 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 85ffc90f-2571-308c-b79e-24577f9ca9bc | 1.86178 | -60.39693 | 2026-03-02 05:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| af6afcdc-ec5e-3983-9f5d-a4d308f60c6e | 3.17246 | -59.90772 | 2026-03-02 05:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9501d43b-7958-32f0-80dc-8539f09d17b4 | 1.51327 | -59.9357 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0183cd1-21c7-3e00-bb54-711f98f1f269 | 1.48633 | -59.93118 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e680f80-ca0e-315c-b8c4-ad422b22d17d | 3.64542 | -61.04335 | 2026-03-02 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0fa5575e-02cd-3642-b1dd-59ea1ade1256 | 3.02592 | -60.68779 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd1a3ca1-050b-328a-9190-335e85bfc689 | 1.50574 | -59.92173 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| abfcdfc9-3cf2-3a60-a135-d679578e70be | 4.2575 | -59.91116 | 2026-03-02 05:59:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2bdff4b2-6368-3090-9d2f-a8a56e14c6c9 | 1.86513 | -60.39772 | 2026-03-02 05:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1ecf2117-6e4d-3e71-82f0-c369f6eef1d1 | 2.85938 | -60.8416 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d567cc4a-b205-3d37-a906-36534c5eedb8 | 1.86761 | -60.40165 | 2026-03-02 05:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 888e11ac-f046-3a44-ba30-0c0a41033361 | 3.41739 | -60.83006 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 968005a4-89cb-34de-832b-544d6f79cdc4 | 1.47799 | -59.93101 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80cba33f-084e-3a7a-9974-b7f8e5ebb7f0 | 3.46083 | -60.78682 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbe94357-a8ed-3688-bac3-e68b2986a559 | 3.41658 | -60.82515 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 848243a0-9543-3eea-b6b5-05ec79c5abdd | 3.0298 | -60.68197 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29f50bca-90ca-3d02-b564-106b30f23c98 | 3.18787 | -60.69016 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6809e430-c213-385b-91be-e0a6cd6dd90f | 1.45883 | -60.07241 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c180e849-06fc-3c73-9f70-4107d63a05a6 | 3.18244 | -60.68661 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9034dee4-3065-32b3-b8d0-49a4c1442b5f | 3.16444 | -60.69486 | 2026-03-02 05:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a7e9b11f-55ae-30d0-9751-8af0b45ee4ff | 1.49192 | -59.93333 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1786f3a9-73ae-3f28-b4f8-ef9e1956b5cb | 1.50379 | -59.90984 | 2026-03-02 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |


[Clique aqui para ver as próximas entradas](README11.md)

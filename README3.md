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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0dc5e83-bcbd-3f46-8ede-e8df69fca809 | -21.30179 | -49.17078 | 2026-03-06 04:53:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d15dd1de-085b-3484-a22e-d4cec1560be1 | -23.27225 | -51.20676 | 2026-03-06 04:53:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| d341709b-9bbb-3b83-b7ec-b6aca82788c6 | -20.63812 | -51.67847 | 2026-03-06 04:53:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8b8d001-6747-3ff2-be7e-dd52fa8afa7d | -20.63754 | -51.6827 | 2026-03-06 04:53:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a38d3e7-1f32-377a-941d-ab79f2c6de3c | -21.71225 | -56.32619 | 2026-03-06 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd2c5c54-fbe3-318f-9a8c-fd289b7584cd | -21.66715 | -56.32546 | 2026-03-06 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2fd7e0a-d1d0-3c88-b415-21ecd8df0cb0 | -21.92781 | -50.66211 | 2026-03-06 04:53:00 | NOAA-20 | IACRI | SÃO PAULO | Brasil | 3519204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6cde860c-080b-301c-97fd-0b9ac64deb9b | -20.20242 | -50.65009 | 2026-03-06 04:53:00 | NOAA-20 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| f48ab640-2ba3-398d-9e15-091be5279585 | -24.05371 | -49.56775 | 2026-03-06 04:53:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 6aa977ba-5095-3c21-af3d-9bff9e97364a | -23.2601 | -52.517 | 2026-03-06 04:53:00 | NOAA-20 | TAMBOARA | PARANÁ | Brasil | 4126702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2dc18cde-5ce8-31cc-bcda-52e9c17ee66e | -29.1829 | -54.91176 | 2026-03-06 04:55:00 | NOAA-20 | SANTIAGO | RIO GRANDE DO SUL | Brasil | 4317400 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 6f621d04-addb-3de3-b6f6-a0f826ab4f7f | 2.7633 | -60.3531 | 2026-03-06 05:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 38.2 |
| c301d579-e309-33a3-88ef-f941e774bba9 | 2.7633 | -60.3531 | 2026-03-06 05:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 5b3796f6-ee57-362a-8d8f-ff16173c7dbd | 2.7633 | -60.3531 | 2026-03-06 05:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 9fa5f4cd-d12e-342b-9514-a1dd45498079 | 4.96498 | -60.26424 | 2026-03-06 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 886a0ddc-aa5b-35a2-a55f-f8858664f1ed | 1.00155 | -59.46904 | 2026-03-06 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eca6aeec-0f61-3dd3-8f3d-8a8981155279 | 3.99879 | -60.16301 | 2026-03-06 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a685030-b80a-3806-b989-9e5da6bb9759 | 1.00764 | -59.50815 | 2026-03-06 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2131b7c-0677-3e8e-b161-47b4da712340 | 3.54093 | -59.91558 | 2026-03-06 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b076b6e-272d-3da0-a7fe-e80b8cf69966 | 2.68948 | -60.64641 | 2026-03-06 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5167eaf2-8e7a-3199-a8cd-09e24d282048 | 4.50952 | -60.54966 | 2026-03-06 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25b53354-8291-3a20-ab83-59045cddd553 | 3.23913 | -60.78512 | 2026-03-06 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0dc029d9-3646-3cbd-89ef-7466f9d645b1 | 3.99823 | -60.15947 | 2026-03-06 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60462b8d-94e9-33d2-874d-e79b49ccb37d | 3.24189 | -60.78113 | 2026-03-06 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 20c686c5-683f-3115-aa6c-d8fcfd4c4b68 | 1.0729 | -59.25111 | 2026-03-06 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5267207-3b64-354a-b48b-2aaa8356d421 | 1.07103 | -59.23911 | 2026-03-06 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c49597d8-b5e3-3b59-bafb-4b1e43a2dffd | 2.7732 | -60.33321 | 2026-03-06 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d9968af-1c48-3db8-9e98-3fe06099d4ff | 2.93025 | -61.05006 | 2026-03-06 05:33:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c0dea5e-1db1-3cea-993e-9f9dae7fa374 | 1.47622 | -60.85455 | 2026-03-06 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b1afc973-987f-3244-86c9-dd7508f385c5 | 1.15934 | -60.89663 | 2026-03-06 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b772d995-ffbb-3e94-a7a8-0be48094cc7b | 0.93884 | -59.34508 | 2026-03-06 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0264cb49-a616-3af1-a306-260f003d773c | 3.25077 | -60.75126 | 2026-03-06 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 519259a3-f8ac-3c32-8c95-61e67d11aeed | 4.82656 | -60.65895 | 2026-03-06 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b98d9447-f1c2-3ae9-a701-bf49f483177c | 1.47288 | -60.85506 | 2026-03-06 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d1f6fdd-0067-3f6d-9fc3-9d0a85ba2e24 | 3.23858 | -60.78165 | 2026-03-06 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 43435cde-2fd5-3701-9056-d93af8d4443d | 2.22708 | -60.22372 | 2026-03-06 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7f3d5dfb-5ebc-3b38-a1d7-f7318e68e201 | 4.96885 | -60.26723 | 2026-03-06 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 185ca91c-75f2-3510-bac2-1443d86feb86 | 3.24134 | -60.77765 | 2026-03-06 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb2b337e-52df-3193-a176-8da7c1d4fe48 | 1.06936 | -59.25167 | 2026-03-06 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 803f6aca-aeff-3056-8a90-d96a17a0d937 | 4.82765 | -60.66584 | 2026-03-06 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f592a44-2784-376e-a772-9c41c8033a12 | 3.5415 | -59.91919 | 2026-03-06 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b51d0ec-ec70-3496-af3b-6e5774d7d737 | 2.23045 | -60.22319 | 2026-03-06 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 421d591d-223d-3256-b0f8-7317a6699ed6 | 2.76482 | -60.34547 | 2026-03-06 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08fb150f-cb09-3e31-985b-3376bbed23e7 | 3.03373 | -60.79983 | 2026-03-06 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8ece745-28e4-3067-9229-5021b7ebc0e6 | 2.76985 | -60.33374 | 2026-03-06 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5415b015-719d-3ef3-be06-32d851b17773 | 2.76147 | -60.346 | 2026-03-06 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e54ad288-c6f8-3f77-bebc-8fc5bd86b3e2 | 1.06874 | -59.24766 | 2026-03-06 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ef56be7-2116-354e-b1fe-910e5af395fa | 0.93594 | -59.34962 | 2026-03-06 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e615612-c371-3eba-ac66-983aeaae2354 | 2.76538 | -60.34903 | 2026-03-06 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f0480b6-b80a-3986-b284-4d664737ad91 | 4.09384 | -60.14051 | 2026-03-06 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6645b30c-7e19-3f21-90c7-971270cdaaef | 2.69281 | -60.6459 | 2026-03-06 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa318f20-ef62-3d12-8ff5-622909f9d844 | 2.52236 | -60.99078 | 2026-03-06 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25a48589-22a5-3e48-b1c6-3b07d30571c5 | 3.65868 | -59.77456 | 2026-03-06 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 302f8b76-a92f-314c-a937-fd4ecf90da0b | 4.20099 | -60.51581 | 2026-03-06 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b9de328-cecb-3edd-a8ac-ef93e823dbd6 | 2.47186 | -60.02201 | 2026-03-06 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59716fb1-ea0c-3f3e-8dc5-b14ff5d5fbc3 | 3.99433 | -60.15649 | 2026-03-06 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e2abe66-9c7f-340c-8cb7-ca547f5bdd8f | 2.76203 | -60.34956 | 2026-03-06 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 28e609c7-31ac-3683-b61f-224a63f944b4 | 4.50566 | -60.54667 | 2026-03-06 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f7ab252-e11e-34f3-b292-49ba1b2a610f | 4.8304 | -60.66189 | 2026-03-06 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c78f8f89-668b-33f8-9bc8-de311aeb1867 | 3.24466 | -60.77713 | 2026-03-06 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fa29181b-50a5-3864-90f9-a11563026a65 | 4.82986 | -60.65845 | 2026-03-06 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7dcad385-b789-31bb-9a1c-ea9bd34ceae1 | 4.9683 | -60.26373 | 2026-03-06 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c755f33-a5e2-39be-98d0-fcd48fd174f9 | 3.04801 | -60.84743 | 2026-03-06 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbb8ba2f-53d1-30e2-ab03-1eebd1325ebd | 3.2452 | -60.78061 | 2026-03-06 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7795e014-86fa-3f7d-a624-45d746cb381e | 3.25576 | -60.73979 | 2026-03-06 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 10cec060-1054-3c6a-b645-31a1505933b0 | 1.06811 | -59.24365 | 2026-03-06 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d236ea98-7bab-3ae0-89d8-bbf8ff823c39 | 3.98325 | -60.17295 | 2026-03-06 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6a09456-ba5d-3413-bde3-c792c6384269 | 4.20153 | -60.51921 | 2026-03-06 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 009bee05-577e-3d35-90d0-39a3a42db733 | 2.47244 | -60.02564 | 2026-03-06 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2f4af6d-54db-3529-a551-b4047bc8a1b4 | 4.96774 | -60.26024 | 2026-03-06 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d60661b-22a6-3e30-9e61-377dd1d3c2e3 | 2.6612 | -60.40139 | 2026-03-06 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4712fb28-8d46-3a1f-b523-0f3ccaf2600b | 1.47344 | -60.85859 | 2026-03-06 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a3524fe-a93a-390a-8ac6-927d50ff74d5 | 4.96442 | -60.26075 | 2026-03-06 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09f465e9-0bbd-305c-bc9d-974730428bf8 | 2.22988 | -60.21959 | 2026-03-06 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 683cc3a2-4fdd-389f-be1a-d1666a8cb497 | 2.76091 | -60.34244 | 2026-03-06 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9bd2c795-6811-32e1-a59b-02b18bc11be7 | 1.07166 | -59.2431 | 2026-03-06 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a583a035-b976-3869-94d6-ec5143715790 | 3.25631 | -60.74327 | 2026-03-06 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdeeb5e5-cb17-3338-b9c0-74e8cb913b74 | 2.75868 | -60.35008 | 2026-03-06 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 501296d3-b055-3100-983a-a58886379e4a | 0.93531 | -59.34564 | 2026-03-06 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd83ca10-ba65-3ad5-b7ce-44c36c3f72f8 | 3.53813 | -59.91973 | 2026-03-06 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ed5ffb3-18b9-3c8e-ac19-65959fc158ab | 3.04747 | -60.84396 | 2026-03-06 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ef3e592-1b6e-3c1d-a154-4b82f335f9b6 | 2.23102 | -60.22678 | 2026-03-06 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9a478b4c-0749-311f-9ae1-b988ab11f9d5 | 1.07041 | -59.23511 | 2026-03-06 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c64ae89-68ea-33fc-b99f-db8deab2a873 | 3.04692 | -60.84049 | 2026-03-06 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07ce533b-28f3-3acf-bd6d-2d5919415b40 | 4.0905 | -60.14101 | 2026-03-06 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bffda680-a579-324f-90f6-c2d555ea3cd5 | 4.83095 | -60.66534 | 2026-03-06 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e12d4b2c-ff2e-309d-8723-f86ae5e2e582 | 4.51457 | -60.93083 | 2026-03-06 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0d62f324-a6fb-3a52-bea5-ebff8d6f3e86 | 4.96554 | -60.26775 | 2026-03-06 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe0dab3c-9682-3534-b850-569103b6407a | 2.92971 | -61.04661 | 2026-03-06 05:33:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6da82604-d0d3-386f-b69c-be0d7bdef2c4 | 2.75812 | -60.34652 | 2026-03-06 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 337f3131-3a9d-37d4-904e-92fc7b6e397f | 3.24244 | -60.7846 | 2026-03-06 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8c990fdd-cf9d-30ef-911a-9d93c8e1f960 | 2.75533 | -60.35061 | 2026-03-06 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 89bf56ed-18e9-363d-a370-dd5ad8b9311e | 1.1081 | -59.56871 | 2026-03-06 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2b2d9a3-7856-3abf-9a08-529e879f9f7f | 2.75924 | -60.35363 | 2026-03-06 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50378917-4512-3496-b58d-58ca4df06cd1 | 4.50621 | -60.55013 | 2026-03-06 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34072959-4212-3bde-8ca3-ee8ae644772d | 2.75589 | -60.35417 | 2026-03-06 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 014754d6-2adc-30ed-92de-1cc328dfa689 | 1.00413 | -59.50869 | 2026-03-06 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28bd2e1e-f52a-38c3-90d3-bdccabb7773d | 1.07228 | -59.2471 | 2026-03-06 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e85ce188-5a7b-35e9-bb53-3dbbee6f775f | 0.99653 | -59.59755 | 2026-03-06 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f543258-354d-3df3-8292-f6ae830def39 | 0.04019 | -60.98328 | 2026-03-06 05:35:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README4.md)

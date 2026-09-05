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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10a268ab-ad76-3039-9a51-868999bea226 | 4.35862 | -59.73507 | 2026-09-05 05:38:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36778897-9dd1-3c96-8f59-be4bef54915d | 4.27659 | -60.04821 | 2026-09-05 05:38:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba280608-c6dd-3aad-81db-32977d1f153c | 2.37392 | -50.76255 | 2026-09-05 05:38:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af2e600b-05b2-3203-ac8b-ab88ba6903e2 | 4.27273 | -60.04528 | 2026-09-05 05:38:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ce32c92-479c-367f-a0ed-114ed9e1c9e9 | 4.94671 | -60.17627 | 2026-09-05 05:38:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f30e56c2-774e-3e4a-a04f-b7e5dc10bf08 | 4.88733 | -60.29602 | 2026-09-05 05:38:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7c96c909-7816-3d1b-bee8-67c1e99533f5 | 4.884 | -60.29654 | 2026-09-05 05:38:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2dd771f3-efd3-3fd1-8fe9-2d26c0610710 | 4.39563 | -59.73278 | 2026-09-05 05:38:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5a2ac2b-cc44-3676-b06a-7651d7148022 | 2.37938 | -50.76162 | 2026-09-05 05:38:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33004eaa-a404-328c-8727-ad85c78ed77d | 4.27605 | -60.04475 | 2026-09-05 05:38:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64ff8bce-cd44-3530-a49b-cbfbac33df0f | 2.36846 | -50.76351 | 2026-09-05 05:38:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9522052a-f67f-3b48-9c52-5cb8dd66367b | 4.36194 | -59.73455 | 2026-09-05 05:38:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5f5b5f2-5e51-34c6-94be-015b3ce05c9b | -6.6698 | -59.9443 | 2026-09-05 05:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 174.6 |
| f311fb65-f333-32f6-a08a-4ccd546a01c0 | -5.346 | -56.0454 | 2026-09-05 05:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| c8be95b9-1e71-3d1e-a333-9720471c6c6c | -6.6513 | -59.9642 | 2026-09-05 05:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 136.7 |
| cb8c94e2-0221-333d-8ec7-37d906d5bf08 | -3.7645 | -61.7737 | 2026-09-05 05:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 6efc7df0-ba0d-39bf-9785-f7a4df1d9d7d | -6.6697 | -59.9635 | 2026-09-05 05:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 126.5 |
| f16f37fd-c791-3710-8f82-3ddb18b6c3c7 | -6.6514 | -59.945 | 2026-09-05 05:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 163.4 |
| 1eeae515-7411-342c-9bb6-197dea7176d0 | -5.3462 | -56.0256 | 2026-09-05 05:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 3e43b064-d731-360f-8970-c154edf180a4 | -4.67124 | -55.63274 | 2026-09-05 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0f18d959-cf6c-3172-9684-9ed48271c0b9 | -5.31658 | -56.02621 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cff96dc9-06a5-3df8-a571-7e8fe90f9f9a | -3.04056 | -59.36157 | 2026-09-05 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3dd267b7-273a-3fe6-8643-1eeb963603ad | -4.675 | -55.63752 | 2026-09-05 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 00514a7a-0024-3880-97da-61ada65c2b10 | -5.32701 | -56.0335 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7a18aa6-0024-3661-a90a-3af564981dc8 | -3.14717 | -60.63731 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f86eee9e-4496-33c4-a483-1369dda2fa26 | -5.32395 | -56.02477 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 247c5702-195f-33ff-b052-17ed90ae7d4a | -3.22904 | -50.57706 | 2026-09-05 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b16a89c5-f3e0-3ede-b648-7dbfd1cd893e | -5.29443 | -56.01631 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b8b41a1-489c-3c91-b298-615fd4b3a67d | -3.78744 | -55.87602 | 2026-09-05 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c65c324c-3661-31ed-a279-a4f57c2746ad | -4.13154 | -56.33463 | 2026-09-05 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a9e9a1f-2497-30b0-938b-caf71b28bea8 | -2.80377 | -48.67934 | 2026-09-05 05:40:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a962ce2-377b-333a-b690-1b7978f71ef7 | -3.38235 | -61.3358 | 2026-09-05 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 981dddce-a614-33d5-9134-3d8ba73c9be1 | -5.29627 | -56.00414 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5b3c4f0-68ff-33b7-8d0c-4be7b5dcfad3 | -3.11935 | -57.69373 | 2026-09-05 05:40:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69fbcd35-7771-3e07-8ce2-5b4e0404f00a | -4.24106 | -62.23688 | 2026-09-05 05:40:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7338289-833d-3ec5-bf06-eb680ee51186 | -2.31577 | -55.25843 | 2026-09-05 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f6a62ba-9e36-32fc-9374-0ff89e9ca5a0 | -5.31104 | -56.02288 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9907e21a-e615-3883-86ae-fba38fc634bf | -5.34551 | -56.03886 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 15107a7d-7b4e-37fc-a760-f0501a2f5706 | -4.67874 | -55.64244 | 2026-09-05 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 510087e4-1c00-36ed-8733-7652e06acbc1 | -3.3984 | -61.34185 | 2026-09-05 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d481955-2e1d-36ed-8cba-f23cfecc682a | -3.80382 | -55.88253 | 2026-09-05 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01e1bcc8-a586-3d8b-b130-55e2c7e65eef | -5.35041 | -56.03541 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| dc5ae644-071c-35a1-b703-ee7bd37cabb7 | -4.91921 | -55.79908 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8c5049d-3e5d-34d0-9091-a6e9b94c41a4 | -3.25584 | -50.82427 | 2026-09-05 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4eb73a88-e37a-370f-8c5b-6c421f00a679 | -3.7725 | -61.75769 | 2026-09-05 05:40:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d388e2ae-c07c-39a7-af5c-4b13b74dcff3 | -3.14496 | -60.6513 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79a83922-2157-3717-b561-71bcb117c19c | -3.42197 | -58.30486 | 2026-09-05 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 511237af-e858-3562-ac39-24fe542ee7de | -4.2803 | -54.77467 | 2026-09-05 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72d35174-f992-3d0e-95b7-f2122abfb05c | -3.07362 | -61.08162 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a3d3764-6cb0-3009-a4d6-a4b1d81fdd07 | -5.15217 | -55.95179 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1aa41c0c-bc5c-3010-bdbc-42512addf8da | -3.07879 | -61.17805 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3944f356-20d3-373a-9753-7f408518c3ef | -3.09376 | -61.19102 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ae8d1b3-3626-3702-b6c4-4568f1ab0a96 | -3.24882 | -60.81048 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f64baa18-1c4f-320e-9094-8944030c39fe | -5.3516 | -56.02732 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 04bcb5a7-0743-3977-a58e-6d2cbc261f1b | -3.40942 | -61.31528 | 2026-09-05 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2bc0b37c-6c24-3814-8a84-4b58d943c216 | -3.63431 | -54.75516 | 2026-09-05 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a92a03f9-a14b-39f7-9416-91ab1d5dd067 | -3.76144 | -61.76303 | 2026-09-05 05:40:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d99aac38-aef1-35b9-9b02-591683b758a5 | -5.32949 | -56.02819 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9fa7e89-6d2e-302c-830d-4712dd297160 | -2.80626 | -48.67346 | 2026-09-05 05:40:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bb5a5165-6f7c-3132-820d-f2e3d2fd8805 | -3.39508 | -61.34134 | 2026-09-05 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de67c428-6072-3d8b-a133-d1fe23ef89d2 | -3.77031 | -61.77151 | 2026-09-05 05:40:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bb603b26-04dc-315b-b6d4-47c484308d13 | -3.22586 | -50.56907 | 2026-09-05 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2795ae48-efb4-370a-9225-505cee958845 | -5.30366 | -56.01351 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b2ce6143-c635-371f-ad2c-292ac32fdf8a | -2.99006 | -60.94825 | 2026-09-05 05:40:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8284b2c8-db6f-3c84-a910-db6ac4149ccf | -3.1483 | -60.65182 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4bb9dee-fd21-3599-85b0-48ab66aae55f | -5.14785 | -55.95116 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df6f5667-0f24-3849-ac0b-7237a49161af | -5.33869 | -56.02541 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ee41452c-31b7-3038-8ce6-e08758abf253 | -1.26466 | -55.7169 | 2026-09-05 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f87b9159-3120-3f27-8850-6440d2cf9fed | -4.19728 | -59.93075 | 2026-09-05 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 95bb5420-67da-33f1-b568-6d003920f553 | -5.30858 | -56.01009 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8e9ed4e-f0e0-3fc8-963c-0244edb7f241 | -5.32825 | -56.02545 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2d5078c-53d7-3a18-bb2d-9634ff66b285 | -4.67937 | -55.63821 | 2026-09-05 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 12cf1957-8c27-30a8-8019-368ae2e715f4 | -5.30427 | -56.00947 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2e5f21e-a304-3daa-a619-7e7cc006e13a | -3.17181 | -61.14664 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d216e300-605c-3223-8989-dc6381f0b8dc | 2.45933 | -60.78064 | 2026-09-05 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88f9b611-9a1d-3022-beeb-d7850776e169 | -3.75921 | -61.75561 | 2026-09-05 05:40:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ea3c59f-d925-3f3a-a9df-cbfea1ca5fbd | -4.15499 | -49.70544 | 2026-09-05 05:40:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 37498703-38b4-317b-9ada-ebb3813c614a | 2.41471 | -60.94778 | 2026-09-05 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ddca2972-2aa5-3907-8cc4-53a42b244703 | -5.32577 | -56.02346 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a869f68-d1b2-3a31-84b4-dfe559ee8259 | -3.77472 | -61.76512 | 2026-09-05 05:40:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cdc249c4-348a-36bb-8dbb-a53766cec155 | -4.09713 | -60.66277 | 2026-09-05 05:40:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2775bea3-ce17-3aba-b8f7-dde4bcfda7f8 | -5.32089 | -56.02684 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fd767a9-f5ff-3c83-bfac-a87029269641 | -4.86956 | -55.86373 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25e12000-25c4-32d1-b62d-59e4642a6151 | -3.79109 | -55.88057 | 2026-09-05 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ef1d867-4392-3d56-b5bd-97cfce6c387a | -5.31775 | -56.01811 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ad32605-0c93-3a33-94bb-3f11592b5f4c | -5.85408 | -52.05158 | 2026-09-05 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76111643-4036-3d98-9b31-37101c730fb5 | -4.91856 | -55.80331 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3655ee31-0b93-3c37-9631-525aa185c252 | -4.47715 | -55.08005 | 2026-09-05 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9344ef68-94c6-3773-a1db-75fd5cba2958 | -5.29196 | -56.00349 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9451eb0d-b502-3391-9e33-71a26da23997 | -3.7764 | -61.77601 | 2026-09-05 05:40:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 42385ec9-38a2-3d9a-8540-228a9fd90de6 | -4.67002 | -55.64097 | 2026-09-05 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bc7bd470-bd39-386e-b806-84f1e9fb7424 | 0.95627 | -60.64888 | 2026-09-05 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47b6271c-f466-3cb4-8776-bd72d5755c03 | -3.08405 | -59.31044 | 2026-09-05 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 051fc4f6-d53d-30a2-9bb7-4d480377f972 | -3.16903 | -61.14267 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 57b04d9f-ec42-3eda-a9c1-9ff9cb7c42de | -5.29013 | -56.01566 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e91eb49d-c88a-3aee-94fc-de3621466487 | -3.38512 | -61.33977 | 2026-09-05 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2e26552-7d35-3282-bff3-0c909ac7dcb5 | -2.81051 | -48.68034 | 2026-09-05 05:40:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 653622d8-fd82-3674-b9c7-b9444c809344 | -5.30735 | -56.01819 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 85e0dd4e-9124-365d-b6a0-673b562c3070 | -2.59042 | -59.40482 | 2026-09-05 05:40:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f46320ab-8c2f-3a83-ac26-0a19bdb01334 | -2.591 | -59.4011 | 2026-09-05 05:40:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README27.md)

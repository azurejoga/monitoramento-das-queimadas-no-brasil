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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aacf950e-6a32-3eaf-9312-cda7eeaa8dba | -1.05651 | -53.58203 | 2026-10-04 05:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b01451a4-96f2-32f6-86cf-455bc51cca4b | -3.04602 | -54.21135 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2cbf6fa8-d3fd-386d-b741-670ec9055fbb | -3.47412 | -54.62467 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5168b9e7-9437-368d-840f-2a756f14eec8 | -3.29486 | -53.84744 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 412b2d42-e8ab-3f2f-816b-dd2aa9339e30 | -4.06083 | -54.31831 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 9dc27cf9-bc9f-3988-9b60-5cd526e7e6d8 | -2.8065 | -54.12433 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fc5457a4-a95f-3ef0-b6e6-20cbbd477340 | -3.8481 | -55.86192 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8c75e05-4dbc-3937-b439-4bb380624a92 | -2.34441 | -57.12137 | 2026-10-04 05:16:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f65a3bf6-e222-3293-b2ea-1d210ac94ea4 | -2.58485 | -51.85231 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5d245dea-4bb0-3869-85d0-a95af5dbee1e | -3.92269 | -55.72831 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6053ee17-81d5-3c88-b09c-9e0b86cc6548 | -2.88683 | -54.14315 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8dd9970a-df8d-3670-8c14-473bdd103f83 | -3.07595 | -49.53825 | 2026-10-04 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 06853f8a-5111-3667-863c-a616a9792b62 | 0.70033 | -51.43663 | 2026-10-04 05:16:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4517b0f9-f743-3508-a5dd-6e3148b895d2 | -1.10393 | -54.14847 | 2026-10-04 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99a71820-f1f7-32cd-93b6-6f392fb5deaa | -3.8732 | -55.81148 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 0b907c99-c6f0-3f66-9942-1c38862f1392 | -5.5102 | -56.06431 | 2026-10-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09b50626-c285-3b3e-bf5b-419ae808bee4 | -3.17939 | -57.91684 | 2026-10-04 05:16:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f121d8bd-74ef-33f3-a08d-53ce1e464f72 | -1.20834 | -55.86372 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 471929f1-8006-3639-bcf7-5c29231505ee | 2.5164 | -60.9972 | 2026-10-04 05:16:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f1267f6f-8586-351b-a1bc-c3fc83458363 | -2.8013 | -54.11148 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 797b0c17-434e-3fea-8b9b-3fa579bd7a99 | -2.91803 | -54.1279 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3634d091-c2c5-3160-a4c8-b0e2205494fe | -2.24823 | -51.93095 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38524032-1e59-33cd-9f92-fdfc3262c798 | -2.981 | -54.09666 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c226d825-bb68-3dee-a181-0b36a606306c | -2.90395 | -54.12575 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 12c5e972-2e88-36bb-ab74-40be3442c648 | -6.00561 | -53.52144 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c17e6bcc-3764-35d7-b4dc-1f48cdfb9cb5 | -3.51404 | -54.61915 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 067268c0-0cc6-3346-b84b-c642b894c7a5 | -2.48356 | -56.09241 | 2026-10-04 05:16:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62067aea-4dc7-3bf4-b899-3de3b78dae68 | -2.90686 | -54.13021 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| da6b9723-185f-3039-8a43-38c829b62bf5 | -4.09966 | -54.32435 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ab2cbbb-b1f5-3d19-a65a-594f22c04657 | -2.81723 | -54.10186 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 46006f01-4a03-3406-bef4-30bb15ee88fe | -6.08461 | -53.30537 | 2026-10-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48e9aba5-4280-3f33-b4eb-767afbca1c89 | -3.12772 | -53.73994 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b24ef4ff-b3a9-3b47-8d43-f815461cfd72 | -1.26929 | -54.56478 | 2026-10-04 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10a2d83e-26f0-3615-b004-214746e64f9e | -4.2602 | -50.73999 | 2026-10-04 05:16:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c5c4970-d278-3d7d-82e9-72cb2e5dd598 | -3.12936 | -53.75282 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c90dc15-25e2-38ac-a4e5-78a971793c3c | -3.0737 | -49.5531 | 2026-10-04 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 23b5d473-abe3-39b8-a5cc-0fddde0c6d3a | -4.2734 | -50.26674 | 2026-10-04 05:16:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d3be7e2e-da1b-3d19-9c75-217b9ed48619 | -2.894 | -54.12019 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4af20f4a-9193-3e40-8aeb-2ed927eecd64 | -2.80818 | -54.1366 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8658aa67-ae1c-3d2e-b0f4-900636641a23 | -4.13235 | -54.16166 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 777e77e2-f8ad-3f60-adca-d14caf12e1ba | -5.99618 | -53.63602 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bcddba92-f26c-391e-9cf2-27f8749a480e | -4.11484 | -54.41168 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4cbba17-4aa1-33b4-bdf3-95d9824ded96 | -3.24877 | -54.51733 | 2026-10-04 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bd90da3-73ab-3c90-b9fc-21510b687b05 | -2.90273 | -54.13359 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0245ac21-8da5-304f-9281-1b91468ddd68 | -3.1308 | -53.7307 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 44a2a6d8-38f3-3dcb-b5d1-f0d465a42a43 | -4.25881 | -46.36375 | 2026-10-04 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e8a1f10a-707f-3261-87bc-369148694928 | -3.13131 | -53.74049 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1cc15840-0347-39f0-82f4-f5925d62c0cf | -2.82136 | -54.09848 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 554959c8-f03c-3c69-80d2-2e1e2f3a93ca | -3.18435 | -50.53928 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e04690e3-1698-32dd-b304-fad122cbdcc1 | -3.46335 | -50.10321 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ea4d938-7459-30c8-933f-1e1fe1fce56a | -2.57772 | -51.87231 | 2026-10-04 05:16:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8b15bab0-51ea-3355-b4cb-1274f0b7c74a | -3.89376 | -49.70221 | 2026-10-04 05:16:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8315270c-fc02-3d6c-afe8-ad510deebe2c | -3.77678 | -51.40389 | 2026-10-04 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 64404017-7b51-3547-813a-0baff7fa209c | -2.80941 | -54.12879 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| efbf1da4-17c7-37dd-b827-edfe07907841 | -2.92842 | -54.1536 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c97a3533-e29a-304f-b368-7f48f4a72ddd | -6.07508 | -53.47051 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3b61631-c4f7-3712-ab62-48e9efcc6a8a | -2.82656 | -54.11133 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e2b2042f-0654-39fa-93f7-8c3b7d9eeaf6 | -2.57824 | -51.86889 | 2026-10-04 05:16:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ec5017e7-c2db-33d0-858a-c0550df2c276 | -2.8995 | -54.08471 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 029444e4-65c4-3132-8691-201fca6d4122 | 1.76566 | -55.63163 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cafc4d19-71cd-369e-82e4-95c8d88c3105 | -2.22295 | -53.71399 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5bc1e038-acf6-318c-a967-e44db82865a2 | -3.12642 | -53.74815 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af51ca29-6e30-3cdd-84d7-1f137e7a6596 | -2.96879 | -54.10345 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97593ca8-ffeb-3667-8aa3-98a70a52f206 | -3.17218 | -54.07642 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63389aff-0374-336b-8e41-d65d03022f77 | -1.09205 | -54.11177 | 2026-10-04 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 172a3792-5313-3507-92d5-4663f4827789 | -3.07708 | -51.28191 | 2026-10-04 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a08c2244-938c-3609-ae43-2959371c490a | -2.92957 | -54.07721 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9b16bd9-a905-3c4c-b6d3-a88ccf3002e7 | -2.92463 | -54.10877 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a1653e8-b75d-31cd-8326-a274586e0ce5 | -2.82761 | -54.12757 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b3a487fd-86db-3f53-a92c-1555a12bac88 | -2.80773 | -54.11648 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 69204fa5-39a1-3278-b1d2-740f64bcb1ce | -2.22422 | -53.7059 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 344764c1-95b7-357a-bfbd-9e5cd541b837 | -3.27886 | -53.83236 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1e94195-b1a4-3fff-99db-586b550287b0 | -3.6171 | -55.50986 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0e621e7-2c48-336c-9ae9-7c07b5c41c83 | -3.1091 | -53.74129 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| f5040f81-a178-3dad-bdc3-4b11668e9608 | -3.22699 | -54.37305 | 2026-10-04 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8de9d0d4-f8b7-3d3d-9be7-a393c08c9064 | -2.9866 | -54.03669 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b0741e2-9969-3f82-99c7-afe0531ba17c | -2.80822 | -58.32986 | 2026-10-04 05:16:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c814b95-66be-3a07-b3d6-eec58b6b9664 | -2.21605 | -51.9568 | 2026-10-04 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| afdeab09-8139-3dc1-a78a-9bc5f03387ce | -3.07938 | -54.37052 | 2026-10-04 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdd9436c-1439-3307-adc1-bdf303ec0356 | -3.65977 | -55.50181 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d9271f7-dc6c-3c2b-85a5-5839e0952609 | -3.04085 | -54.19852 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8b8c5c3-812f-37ca-9133-02d551327bc8 | -2.80237 | -54.12771 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a1f7c3fe-aadb-3ba6-89e8-d194916a219e | -3.4686 | -50.0993 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 44368572-936e-30b1-bbfe-c64fc06f5fc3 | -1.10107 | -54.14418 | 2026-10-04 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1196afdc-e993-34a9-a13f-38bb384571f9 | -2.93168 | -54.10986 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41719aaf-d029-337f-bea2-e5aae45513b6 | -1.81557 | -59.93082 | 2026-10-04 05:16:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14935785-9874-30be-88ec-8d2983bfc6b7 | -2.20988 | -48.22779 | 2026-10-04 05:16:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84e6604f-3da8-3eee-87a5-85253dace1f5 | -2.90824 | -54.09816 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8c784f4-207d-35cf-a4fb-6276f19d9c1d | -2.90011 | -54.08076 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b7b040fe-a4e5-38b7-8b98-fdf9bdf7274a | -1.09837 | -54.11663 | 2026-10-04 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1ab56927-792d-3e58-ab23-893014450860 | -2.9816 | -54.0927 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f5013616-ea17-36da-85be-a03a99e835d5 | -3.46597 | -50.0905 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 788f9586-882c-3825-a84f-a0324fa710fb | -4.11132 | -54.41112 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f53edb85-489a-3490-a0dc-0e3782ed6d2b | -2.80421 | -54.11595 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 74066a89-050a-33cf-af2e-bb4e1ae96456 | -4.28564 | -50.27807 | 2026-10-04 05:16:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 56240e0c-c850-37e3-b032-cb2e61fdbcb2 | 1.77345 | -55.5953 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2af5a72f-1987-3711-8299-208338593815 | -2.96507 | -54.10632 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 498a8353-8c61-3bb5-b209-0e23038e9ce3 | -2.90563 | -54.13805 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| cc500891-1720-3784-9fbd-58b0a3429b50 | -1.08573 | -54.10692 | 2026-10-04 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41d250d4-d505-3e7c-bbe0-c764869ef8f1 | -4.26729 | -46.37153 | 2026-10-04 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |


[Clique aqui para ver as próximas entradas](README56.md)

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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7fb84960-5a2f-3d03-b64e-cf981affc7ca | 1.28559 | -55.94229 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1bac618e-a600-38b5-9939-08186b8cea62 | -2.78254 | -51.93219 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9238b58f-8ce5-3870-b39f-3fabe5030cec | -3.24748 | -50.59191 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bc5fe405-84f5-3556-9ee0-51c13bbdcb56 | -1.27212 | -52.11901 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 107813a8-37e5-359d-9833-322f6a41bedb | -1.72042 | -52.49368 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 22f2b89d-cf18-3e91-a097-598f512353bc | -1.05599 | -52.415 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1662e65-13e5-316f-ae80-341713dd28fd | -1.55702 | -52.01799 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47636c74-e191-36f7-8288-5b5b4bdd25ac | -1.3477 | -55.00859 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3bc2c672-6b6a-336d-8079-730a4bfc63e0 | -4.07101 | -54.56374 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 747aac66-094f-36a7-8482-c15a2803cd7e | -4.26524 | -42.60613 | 2024-11-29 04:57:00 | NOAA-21 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 008e5675-2a77-3d4f-90e3-d66f04f741a9 | -1.18026 | -53.88675 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 222c3952-70ea-38d7-a37e-27d899397aa2 | -2.44342 | -53.96435 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d65ab30c-763e-3358-ae6b-a07e20530338 | -4.43973 | -46.58846 | 2024-11-29 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| a1ec5e58-4091-3a5b-a659-0a52c7d75d11 | -1.66224 | -52.7365 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9a2b072d-dd47-3b99-b6e5-ad06f2270559 | -2.62022 | -51.75441 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57b42fa7-818b-32da-a0f9-14e9a54853ad | 1.97151 | -60.91693 | 2024-11-29 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9941c2ba-fa78-3c07-9248-2f459563268b | -1.1537 | -51.70318 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 762d8ef7-6c85-34f5-bcca-185d806a738d | -3.27888 | -51.28297 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 403ea75b-5782-343d-a77a-f17f031988c6 | -0.95409 | -53.20055 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71158bec-b0b0-3ce3-ac45-38490f7465d3 | -3.57924 | -53.26941 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97ab9ade-75c7-3ba2-a94e-1796d3ac450b | -1.11055 | -53.22113 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8832820f-51ee-334d-aa5a-222b3eca7c79 | -1.56402 | -53.52083 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9fb77de-735d-3c17-8bcb-a06f5f1adffa | -1.07828 | -53.38462 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b146b86-b256-34d3-92c7-888f550f2811 | -5.75457 | -46.26556 | 2024-11-29 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4f6d44e3-c816-3036-8e6c-b05d8066c513 | -3.17468 | -46.3056 | 2024-11-29 04:57:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94925cd9-cb5a-3689-ab42-07caba460f38 | -2.8748 | -53.99009 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a9a19661-7e45-3da4-9ebf-4f4d0dff5872 | -2.65527 | -49.51686 | 2024-11-29 04:57:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8f3d09e-8b7a-348b-9231-c6cf07c29be1 | -2.36834 | -55.70638 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d596aa64-1835-3b65-a4b4-dfd25279e262 | -1.28462 | -51.72694 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a8f77228-6c90-347a-b61b-a6f25241b63e | -1.13713 | -53.79122 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20238193-b302-3a78-b721-f18a75cddc0a | -1.29971 | -55.74426 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 15c611c0-a8c5-3130-bd9d-4cd83f42eca1 | -2.69926 | -48.65068 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9fefec1-e2d2-391d-b5a5-9ec63a7af8d8 | -3.32964 | -46.7 | 2024-11-29 04:57:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cce72f1b-dadf-3fec-ae74-48c68ed8e279 | -2.57 | -49.07727 | 2024-11-29 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8673921f-dbcd-3b53-9730-bfb3e68d4c54 | -1.47808 | -54.43998 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f36de90c-47f2-3b5c-9ddc-d28336fc7800 | -3.43878 | -50.12283 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b1d4e6b-c891-341f-afb0-cb693b5c2c0a | -1.44892 | -52.99304 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a71c869-51b8-3862-b583-55bc188bb76f | -2.83922 | -54.04451 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 043f75e3-7574-37c7-9c4b-749a9fff50bf | -2.81776 | -54.05178 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8bf291b0-a7f5-30f1-8885-57e8f370850c | 0.94444 | -50.73285 | 2024-11-29 04:57:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a7a4760-9931-3811-aef7-d2cc06d0d14d | -1.57195 | -52.00189 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1c4d52c1-af8c-3118-ab40-ce9d15246f79 | -1.07872 | -53.36013 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4a41f7d-18ad-39dc-8d88-d03b7ab5b45b | -2.6279 | -54.02523 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 70d3a2d1-0e0a-3389-8998-5007878c052e | -2.84184 | -48.09113 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f69bfdb-d046-3f26-80af-7ec682ccdc4c | -1.3356 | -51.41781 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96bffb9f-7565-3b42-897a-55c7203fa1bf | -2.72982 | -48.89449 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 401ae07a-9e1b-3aed-8fe4-22de0ec5729f | -1.22559 | -51.80654 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a4f23ea-6f7b-33fb-940d-be4608c3bc5e | -4.91541 | -44.03005 | 2024-11-29 04:57:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84a0115c-f061-3e2e-b92a-e2dbbc0c7a7e | -1.22084 | -54.1914 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04c4dff0-d610-3a45-b576-6eeaed49fd35 | -1.09086 | -53.36901 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ec6c5e5-e251-39fb-8c71-1db3171cf5d3 | -1.16049 | -53.57647 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5aadc518-3dc9-3d05-aace-182f0b393571 | -2.66961 | -53.03898 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4c6bc4c8-f3e1-381e-a712-fa9820891eae | -2.62006 | -53.98875 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 85342a15-3813-32d9-b4b6-d785efbe044d | -3.11081 | -53.98502 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1bade012-0a0e-3fc0-9ab2-5efaba65b727 | -1.53313 | -52.69191 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ddbdf7f6-a2f3-3ed8-9976-bab551e7f109 | -1.10586 | -53.4029 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 874d99d1-35bc-3474-9ae5-1791ace64e2b | -2.69765 | -48.66118 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77f88e76-3410-3f8e-bd68-a8a5f4a4bb8a | -1.1808 | -53.88332 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 240c93a3-cf01-3c8a-9bf1-25741380693a | -1.94909 | -52.96863 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 534dff8b-1aed-3c62-8a5c-4048c6150bfd | -1.5309 | -52.68447 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06674eb3-f9e5-3b8e-a338-c1e6f3c5f323 | -1.71532 | -53.24921 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fac9f33-4010-37ac-92f7-854462ff2726 | -3.28849 | -50.5173 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc7dc608-c1ea-365f-8ba8-1abcc0c31d4d | -1.6968 | -52.45018 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 353f3e0a-6763-30d9-adf3-037f61bf25d0 | -2.7963 | -54.05905 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 850fcb1d-65de-3af6-88c4-c5db76b44244 | -1.31787 | -52.80661 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7967f748-ab51-3bfa-8a28-685de357fda5 | -1.30492 | -55.74438 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 63bc056b-5299-3587-ae4b-067cf1ca334b | -4.4867 | -48.11397 | 2024-11-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| af3d877f-93b5-3c78-85c8-45b8172a0ae5 | -2.9009 | -53.06044 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c83de338-2311-380f-9f52-bb17da0edf36 | -1.15682 | -53.62164 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29838499-9d53-3e2b-974e-5b3173d1961b | -2.85058 | -53.035 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90253a96-0273-3cb1-b869-9a74028bbc91 | -2.44843 | -54.02217 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8779a026-7216-32a6-905d-6c9c568bcf6b | -2.36126 | -48.54588 | 2024-11-29 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71140258-09e9-3933-bb9c-6863b850bdad | -2.9855 | -53.34954 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ee3d3e9-b633-3fa6-8c0a-5c51c0d7a69f | -1.23728 | -51.62018 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86d25bb1-7966-3b9e-8018-fe86ba834f5a | -1.6231 | -52.46386 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b81b3599-5f6c-300e-995a-91ea6065f6d2 | -3.23703 | -53.63168 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95ce7474-ccf5-3155-8467-851f975b8879 | -3.04922 | -48.51518 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d79abcf-16e2-30d3-9add-1c1121cb4e62 | -2.01213 | -51.1899 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4c212d80-2dee-3619-bf60-db0cbaf8ae9d | -1.08712 | -53.393 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0531d851-91b4-3f4a-a0c6-43efa418c5eb | -2.82707 | -54.03559 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 726ed007-1d01-3fce-a776-a3208805d7e0 | -2.8689 | -54.02794 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f895bc9-4eff-35d4-9fa3-85bf0d099cbe | -2.24292 | -50.47934 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49c53eee-0097-3c9c-b770-cf35fb850bde | -2.27239 | -51.32583 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b446b6a2-624c-3771-a9c9-81abb3d5b277 | -1.48022 | -51.95878 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de67e5e1-5568-3168-b96d-efd56311c791 | -4.24183 | -54.7326 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19a0b88d-0fd4-3e59-9f42-5dc030aa14ed | -2.89156 | -51.58689 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5d4cb88-e96d-3c94-aa18-88814d8b97b4 | -4.07264 | -54.87809 | 2024-11-29 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f4cc6d7-0b91-3581-b414-daf72e414ef6 | -2.84653 | -54.08444 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 181a98df-efa2-394d-b494-2e2d9b043d5e | -4.4368 | -46.58372 | 2024-11-29 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 0058366f-9b7e-3358-8104-3681f3566be3 | -2.61909 | -51.76175 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 17beb174-ebf5-30ec-95c2-5ac3ac2e8f49 | -2.87927 | -54.00487 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84882979-7c24-3bc5-a5af-46f19f649938 | -2.75365 | -54.06934 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 61038c75-8521-359e-b7c3-f85cba5b4364 | -3.78506 | -46.69002 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 986dec42-fbf2-3677-b598-b15fa080bc36 | -2.82661 | -54.0602 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d916bd7-789a-3069-b577-9ea9e5014583 | 1.26174 | -55.90759 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 20aa433b-66c2-3026-adef-c43670204990 | -1.16148 | -53.54851 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f43f3be7-0c38-335a-90cc-d56592014895 | -1.13166 | -53.39296 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c91bf7f3-d3c0-3ad2-b878-3b0912c6124b | -3.00783 | -51.02044 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2caa9e76-02bc-3db8-b4d6-cfcdadb9b89b | -1.20023 | -51.74753 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ee219770-fe80-32a3-9581-4b02da478d56 | -4.0004 | -49.97309 | 2024-11-29 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README47.md)

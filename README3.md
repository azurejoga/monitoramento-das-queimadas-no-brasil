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
| 5479c783-6598-3a2d-930b-a05f56ccb87b | -2.0714 | -47.857899 | 2024-11-25 00:04:00 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7acc7718-872a-3224-b224-74440c12750d | -2.8181 | -45.124901 | 2024-11-25 00:04:00 | METOP-B | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9ec4071e-e0a9-31b0-a351-23183048eac5 | -3.8022 | -51.151501 | 2024-11-25 00:04:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95150a8a-1d17-3077-83e3-e354228f3587 | -4.0486 | -48.305 | 2024-11-25 00:04:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24f0dada-f7c4-35c7-ae64-2ee789c28eec | -2.9647 | -45.7798 | 2024-11-25 00:04:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9e0e8e33-5072-35e2-a284-5d7cc20a24d4 | -0.0538 | -50.798698 | 2024-11-25 00:04:00 | METOP-B | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 866f7175-5dbb-3ee0-9ddf-7065de8ad5e4 | -1.7165 | -52.6917 | 2024-11-25 00:04:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df98cf15-4d81-31c6-953e-79da3c2f387f | -4.2409 | -48.574299 | 2024-11-25 00:04:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16db742b-e10a-3f89-9743-95adc06ef45c | -4.0265 | -48.0644 | 2024-11-25 00:04:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85311a81-1190-3b11-9962-71414248c0e8 | -0.2747 | -51.592701 | 2024-11-25 00:04:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| f7fbd046-849a-39c4-958e-25e38ab398d2 | -4.2599 | -48.707901 | 2024-11-25 00:04:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05b9b1fa-8dc2-35f4-af2c-85d6e0717a61 | -3.5709 | -45.4524 | 2024-11-25 00:04:00 | METOP-B | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c6122256-1a80-3b8c-b8e1-ad636997a837 | -2.9001 | -51.5481 | 2024-11-25 00:04:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00209f44-d77c-33d0-a30c-b7d4446cd7de | -0.0508 | -50.785599 | 2024-11-25 00:04:00 | METOP-B | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 007d5f98-d6b4-326d-aded-3afb9224590f | -3.0563 | -53.185799 | 2024-11-25 00:04:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d45ca133-1b18-3f73-986d-89ad803d79f1 | -3.4956 | -50.448399 | 2024-11-25 00:04:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e06321e-6a26-375e-a215-822b8ad5c5b5 | -2.8448 | -45.473701 | 2024-11-25 00:04:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a03cc710-d912-3aea-a7bf-ff13b5fff20c | -3.2773 | -51.082802 | 2024-11-25 00:04:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c56a22e-4264-3351-ae71-ee35449bc4d4 | -3.7143 | -47.1152 | 2024-11-25 00:04:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70ef1b3f-8de5-318d-925e-5e964ce5a248 | -2.5762 | -45.9753 | 2024-11-25 00:04:00 | METOP-B | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 106666e2-f61d-393b-8e5f-785708d1dce6 | -2.91 | -51.685501 | 2024-11-25 00:04:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d13b45e-f6b8-3f2e-a4e7-f9b90ea73b3f | -3.4818 | -49.873299 | 2024-11-25 00:04:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68f5819e-db92-3d10-928d-80312b51fdaf | -2.9002 | -51.687599 | 2024-11-25 00:04:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d62c4990-0aff-3e8f-88ff-173b12bcbb5a | -2.3362 | -53.833401 | 2024-11-25 00:04:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e9a97d9-4f57-31db-85c4-b3f3f3fa6885 | -3.7007 | -47.0998 | 2024-11-25 00:04:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5988cb1-3adb-3dd8-986b-92dc385e4c32 | -2.2941 | -45.3601 | 2024-11-25 00:04:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 49b7a614-18af-3061-bde1-8f27050d9bb1 | -2.3163 | -53.789101 | 2024-11-25 00:04:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8909e6c2-ce58-382d-887a-dfa4526eb67a | -3.1866 | -49.044201 | 2024-11-25 00:04:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73c9721c-1f3c-36db-8be0-d826b55fb30b | -4.2575 | -48.6968 | 2024-11-25 00:04:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7517bb91-6ec4-3a78-92e7-83aa82d2e643 | -2.9168 | -46.671101 | 2024-11-25 00:04:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa56e080-fa95-3d1a-a6cf-58da87cda653 | -2.0734 | -47.8671 | 2024-11-25 00:04:00 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 606a0eab-e80d-304c-a87c-350487de435a | -0.752 | -51.713001 | 2024-11-25 00:04:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 03c46bb6-232f-3057-bca7-7817fe7d3d63 | -2.3117 | -53.814301 | 2024-11-25 00:04:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55de852c-7497-32d2-8cca-33e632d79c19 | -2.5778 | -45.9828 | 2024-11-25 00:04:00 | METOP-B | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fa6c9693-22bd-33d9-9f0d-f99d74953bc4 | -2.3311 | -53.8102 | 2024-11-25 00:04:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd750da0-4b24-3bc9-a501-d0845dfdb8a5 | -1.7693 | -52.7001 | 2024-11-25 00:04:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7731bac3-efff-3d88-8c21-978ebd9092f7 | -3.7105 | -47.097698 | 2024-11-25 00:04:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84a11fe3-b94f-3206-a539-8a4779efa31a | 0.9743 | -50.112499 | 2024-11-25 00:04:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| db339043-9a63-3857-896d-83c374a3801b | -1.2929 | -51.710201 | 2024-11-25 00:04:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7dcc7325-df4d-3dbc-8543-db5c28182ccf | -4.0243 | -48.054401 | 2024-11-25 00:04:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fa1b887-c463-3d13-97c9-93499528bb13 | -2.3265 | -53.835499 | 2024-11-25 00:04:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34ced156-fd8d-3fcf-a9e8-94b45df8c8eb | -3.6325 | -51.121201 | 2024-11-25 00:04:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7c3ad7a-3878-3e0e-8995-3dd80ce06983 | -1.3716 | -52.288898 | 2024-11-25 00:04:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e7eea7a-82de-33f5-ae28-d900b41310c1 | -3.7026 | -47.108501 | 2024-11-25 00:04:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe3b0cbe-9948-3aca-959b-740e8baa5b01 | -2.2369 | -53.568298 | 2024-11-25 00:04:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e45ef0f0-9dfd-3e59-9f2d-bfff6eade3b0 | -4.4123 | -49.6875 | 2024-11-25 00:04:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 019ae010-01a8-3ae4-b50f-4f80a57d0571 | -4.0363 | -48.062302 | 2024-11-25 00:04:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92168bd5-a5fe-35c4-be52-d95d94a8f21d | -2.2516 | -53.588501 | 2024-11-25 00:04:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fb0a27d-1800-3eb0-bd35-d017fa549d4f | -2.9382 | -50.979801 | 2024-11-25 00:04:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 010763eb-fd85-3856-9c0b-d07dd7ed54a0 | -2.2466 | -53.5662 | 2024-11-25 00:04:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f03f6842-8c34-3aa4-a05d-c681b8ff4d0a | -2.3214 | -53.812302 | 2024-11-25 00:04:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b19f55fe-7e60-38ef-841a-ad72597f3cdd | -3.0681 | -50.920502 | 2024-11-25 00:04:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81fddbbf-b6d8-3837-835f-0bd4124be8d3 | -3.5008 | -53.7831 | 2024-11-25 00:04:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68bebfda-56b0-3db0-bf70-57672a6268c2 | -0.96 | -51.683701 | 2024-11-25 00:04:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d967272-006e-30a8-9f9c-00fdae014b23 | -2.9349 | -50.964802 | 2024-11-25 00:04:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 728b6ba0-3ac2-3b99-9d13-04b892e8bdee | -2.9664 | -45.7873 | 2024-11-25 00:04:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 29eebcd0-06e7-32cc-91a6-f334211b8148 | -3.2841 | -51.113899 | 2024-11-25 00:04:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa23e410-7364-3f84-8bee-de6d763ee577 | -4.2433 | -48.585201 | 2024-11-25 00:04:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2ae3c52-8241-37f2-aea4-5436f5d0eb10 | -2.3168 | -53.837601 | 2024-11-25 00:04:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb43f5c7-d9eb-3949-a15a-635543618274 | -0.0568 | -50.811901 | 2024-11-25 00:04:00 | METOP-B | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e45fc8f-5b0d-33a8-a2e2-a5900fe2ddff | -0.0441 | -50.8009 | 2024-11-25 00:04:00 | METOP-B | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5781b13-6531-3492-a493-9868808739c8 | -2.9063 | -51.668701 | 2024-11-25 00:04:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70313275-27ac-3dcb-abae-d4ec0cb66796 | -4.2309 | -48.622101 | 2024-11-25 00:04:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a168daa2-80c1-33cd-a2a4-aa4064811084 | -2.8909 | -45.3116 | 2024-11-25 00:04:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7a25fa83-de3d-3ca7-a5f2-b7b20503f951 | -3.4894 | -50.4203 | 2024-11-25 00:04:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad0f237a-5073-329f-81da-1f0a9ebf4c7e | -3.7208 | -51.152199 | 2024-11-25 00:04:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc588a2c-4882-3aa6-a4f3-0f31d251a5ab | -0.2713 | -51.577702 | 2024-11-25 00:04:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 0b743d32-28bf-3bf8-bbf5-0a1c18962a2a | -2.5458 | -45.380001 | 2024-11-25 00:04:00 | METOP-B | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 64d1f804-5f97-3883-a3ae-9a3b48e99cdb | -2.8868 | -51.533798 | 2024-11-25 00:04:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e4b1c19-5e87-372d-a558-0ba2ba6db5b0 | -2.1708 | -50.5597 | 2024-11-25 00:04:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cf57ede-f628-34bd-a61d-fbd4d2847a30 | -3.0515 | -53.164299 | 2024-11-25 00:04:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea0e9a27-fcfe-3b31-8fa4-d46ff1d99121 | -2.3317 | -53.858898 | 2024-11-25 00:04:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64bb0eac-c1c4-34fb-b40b-d5b8fd217d54 | -3.5105 | -53.780998 | 2024-11-25 00:04:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32257f8f-679f-3c83-88c9-d0e838d77ed9 | -4.0287 | -48.074402 | 2024-11-25 00:04:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cc81766-326e-32ed-9419-f966c799aeb3 | -3.7124 | -47.1064 | 2024-11-25 00:04:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5f2ac0f-79fc-3e92-b4ac-0077c4424592 | -2.2925 | -45.352901 | 2024-11-25 00:04:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 40d87de9-6a14-3f45-b9e7-09b4d6ce4fe7 | -2.8013 | -46.799099 | 2024-11-25 00:04:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 927a9e40-0690-38af-86f3-a8e7ddb00ffa | -4.0189 | -48.076599 | 2024-11-25 00:04:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 247a4828-f834-31ff-8f3e-1c8e9aa17d77 | -0.817 | -48.0853 | 2024-11-25 00:04:00 | METOP-B | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d29f42d9-89ca-3f4b-b653-c8c78463772c | -1.1409 | -47.696098 | 2024-11-25 00:04:00 | METOP-B | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f841ef1-d2e4-38f9-9640-db0874149364 | -2.2419 | -53.590599 | 2024-11-25 00:04:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f901bc43-a70b-3d86-a0b7-23c16c8058b2 | -2.8197 | -45.132 | 2024-11-25 00:04:00 | METOP-B | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1bc36371-b1f6-3882-a9b4-d118b8d10c7e | -2.8893 | -45.304401 | 2024-11-25 00:04:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5fce3c2f-d9a3-35cf-9747-cf0fdcd2e3c0 | -3.4925 | -50.434399 | 2024-11-25 00:04:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fd0e901-a46b-34f4-8ae5-c4cd5979e561 | -3.5315 | -50.426102 | 2024-11-25 00:04:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cae7f17a-2810-3671-bd76-1282d72b6211 | -3.5414 | -51.497501 | 2024-11-25 00:04:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50b4d82b-0501-3c02-b08c-368c22adab63 | -2.8925 | -45.318802 | 2024-11-25 00:04:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a324bd86-72cb-3653-804a-4bcb548021d0 | -4.2502 | -48.709999 | 2024-11-25 00:04:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4854343b-d663-3ac1-bebe-b3b768640824 | -2.9211 | -51.736198 | 2024-11-25 00:04:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cc7088c-34fc-3045-af33-97af82f81346 | -4.0045 | -48.0835 | 2024-11-25 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| ac91f7a9-d6d3-3f4a-821c-461c86ad4c7d | -2.3211 | -53.862 | 2024-11-25 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 269.3 |
| 83cb9a25-a86f-370d-a3fe-d0ef3d459ff6 | -4.4845 | -45.5478 | 2024-11-25 00:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 125f4bcb-5975-3b50-8dda-46fcf7055219 | -3.7129 | -47.116 | 2024-11-25 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 601f4947-cb4c-34b0-b653-8f26332974fc | -0.0644 | -50.8171 | 2024-11-25 00:10:00 | GOES-16 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 140.4 |
| ab153169-f46f-34cf-afa9-18acad6e46d6 | -4.466 | -45.5263 | 2024-11-25 00:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 71.8 |
| e5d75577-4500-38f1-83c4-2c6fe7fe29fd | -3.9494 | -47.9776 | 2024-11-25 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 0f17374f-713a-3539-902b-65a5dcbadcfa | -3.7058 | -52.4055 | 2024-11-25 00:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 2d7588f8-ef19-3e59-b0a8-c98b7eb59b14 | -0.046 | -50.8171 | 2024-11-25 00:10:00 | GOES-16 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| d5235623-21fc-3fc6-bfc3-1648ca029db4 | -4.3147 | -45.8928 | 2024-11-25 00:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 80acb961-7658-3397-9e69-d9168b97cc79 | -4.023 | -48.0827 | 2024-11-25 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 163.6 |


[Clique aqui para ver as próximas entradas](README4.md)

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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e496fdc-717b-3a6a-b822-892b153bc3b3 | -2.93687 | -54.15121 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36e768f2-3086-3d09-ace0-2ecd0abb55ce | -4.06723 | -51.03923 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dee58fdf-5155-3444-abbd-1985b4986ff0 | -3.51146 | -59.9467 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8211f95-906c-31b2-a783-0fb380db36c4 | -3.68332 | -55.95455 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0aa5efab-e3df-3386-815f-70c91d7059bb | -3.02048 | -53.917 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a4afe9f4-3d6c-35e6-a80b-819676852371 | -3.07159 | -59.27748 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4fd06240-4bb7-3bd5-89c8-8f21d468e240 | -3.4001 | -60.85098 | 2026-10-08 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eacc9f96-25ae-3aeb-960c-45d000d478fc | -3.08974 | -53.95992 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8337c855-beec-34ae-916a-f1500227a1c6 | -2.47016 | -56.07727 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44b45c10-1fa6-3554-af3e-50f4f2f45ce1 | -3.21208 | -53.86839 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d681807-2167-351d-9061-c34cb69b6b51 | -3.00031 | -54.1175 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c24f5796-aef9-3bfd-95b1-06e15fdd6d47 | -4.80794 | -54.6782 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 729820da-5984-3985-a11b-25ca946b9c1b | -2.76813 | -54.0993 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57a98bd6-8d59-3b47-afca-b5c184723f88 | -3.70122 | -54.19715 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0882acf1-5c7e-3c00-9399-b74b5ef7f20c | -3.01252 | -57.90539 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c92a8717-14fd-3648-8a21-4df71f5e1053 | -3.84154 | -55.98632 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c22e5980-7d46-3cfc-8158-59067b5a7312 | -7.18193 | -52.62175 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b7c92a2-e202-3912-83f6-72f7f0c5c309 | -3.95715 | -56.11143 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51ace709-2c5a-325a-8a85-04651f4e9919 | -3.20501 | -50.55687 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3565e203-04b3-3bbf-b44d-8987220ca389 | -4.29896 | -54.8044 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b34f9193-bc57-32a1-97f2-ade486b0aa38 | -3.83541 | -55.98178 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6e050a0-ad44-38a5-ae79-fc335bbd4a85 | -3.26682 | -54.02542 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4026931a-46c6-3fd2-81f4-a84b8461af3c | -7.08093 | -52.68375 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 972d905c-732a-3d33-b147-13ba86267d9a | -4.46194 | -54.97412 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf230cd7-a690-33a8-a961-294dec0e8290 | -7.20469 | -45.35006 | 2026-10-08 05:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 71a16b54-0993-36e1-9ce9-c37fe5ee6693 | -3.5667 | -59.49236 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6647885a-44ed-38c2-ac79-2cd255ed4506 | -6.1226 | -53.05598 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38fc9bb1-d8c1-3c58-b2e1-4bc0f64f1431 | -3.01081 | -54.11914 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| b7f4ff4a-020b-31e7-9e9e-d7a7dd2ccc08 | -2.8996 | -57.65349 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebc5b0cf-9e3c-3832-9b8b-3b04dddd6c2d | -4.56382 | -55.05748 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0041542-6441-3007-96f5-ecc1573caf7a | -3.26317 | -54.04879 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d6bb4244-e5af-3215-9c28-2189763ca781 | -7.22016 | -55.10803 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| eed355cb-ba3a-3d43-8468-7846d0f1b98b | -3.04325 | -53.95676 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| da555209-c551-301f-aacd-3521fa76538e | -3.30143 | -54.696 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1236f97d-8d50-3347-b3bf-857c40d9bf71 | -2.78587 | -56.49874 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 769ffc34-9da0-37ef-9485-e0b686df2856 | -2.98108 | -54.10264 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98ccf631-8585-3bde-b675-b6bcab63cd56 | -3.28338 | -54.01191 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0949bd2a-979d-3bf6-a9c4-b77a06e440bb | -10.61727 | -60.49016 | 2026-10-08 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ea4be63-2711-39ef-9b63-08f360379246 | -6.52473 | -55.27417 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 40781692-2252-3017-915a-f764fe0ad49a | -3.10156 | -54.18341 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 63548d56-1d7f-3c3d-9686-a6283e682619 | -3.96272 | -56.11944 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6ecdedb7-dc69-3be0-8bfe-80a40c55aab2 | -6.10419 | -55.71387 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c67ebd3-23ec-3733-a5cf-f67d1a836e2f | -3.0093 | -54.05943 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 3e998423-146e-3a85-b321-c082bd665cf1 | -3.27115 | -54.66468 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a6e88f6-260b-3694-b2f7-dde3ea87ebf7 | -3.02505 | -54.0738 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a4441eea-899c-369f-961f-db68cbfe2ba1 | -3.0167 | -54.24201 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de9e11d2-e7ee-3b56-8b13-d77d3db5a91c | -3.9273 | -50.33783 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 2e03f3b3-7c73-3fa1-ba31-62af0f1ec610 | -11.86234 | -48.03273 | 2026-10-08 05:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82ffc97d-7a06-331d-96bb-ff459872e6b1 | -3.21091 | -57.86637 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f426dd9-a816-348a-8562-619a0820fe0c | -3.01997 | -53.89676 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 592bd18b-cb03-3d27-87a2-e023bd6c4795 | -2.4785 | -56.08921 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73d61642-cda3-3ce3-a8b7-330d0f1005e9 | -3.86824 | -55.96906 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9fbba41-8e4f-3be5-8cac-43f22b51c1f4 | -3.00279 | -54.07827 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| c657dd47-c164-38ff-bcb2-307bb193276f | -2.81369 | -59.24796 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3966508-b4af-3bb5-be1c-b09c63be00c1 | -3.95828 | -56.12588 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0fe7a0d3-2869-3d36-b611-7ca0a5258a65 | -3.30394 | -54.01904 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa90a036-5b25-3257-b420-234fedbafe05 | -2.78203 | -54.08483 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 27eed50c-f196-3a4e-82d7-8edfc50fd8e0 | -3.6744 | -55.946 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d19917a1-50fd-3883-9f4b-47910f644b88 | -3.07979 | -54.25471 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dca2d5ff-10df-3972-9f1b-1028eb4b22ae | -3.08926 | -59.19056 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f559ad3a-58a0-36d9-b659-5c4e9617cfc5 | -3.53094 | -57.53183 | 2026-10-08 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd6189f7-12db-3bf6-87ea-ceff9fec31a9 | -2.79133 | -54.09417 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e499f81-3d26-325e-8e6f-8e80a6496581 | -3.83985 | -55.97533 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4d85e2ec-83d5-3ba1-b9e7-b20632f1887c | -2.94829 | -54.19227 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 044be283-a6ab-308b-b7b6-5a3e2bb62125 | -3.00288 | -54.05445 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 71d27228-8428-36f6-babc-fdaaee0c8bc9 | -3.22009 | -53.4157 | 2026-10-08 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de9f5efe-864a-36ce-932d-0f69b12e5c4f | -8.52361 | -66.99812 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66fef422-333d-3f88-b226-b8b5f41388b3 | -2.48575 | -56.10806 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 693763b2-1182-3b54-abe2-d1ad6f7ccba9 | -2.76342 | -54.10644 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 929c670e-fc68-3150-8398-b4fad5ef9b97 | -3.67998 | -55.95403 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 167ef420-4640-3ae9-8bfe-a0f07b239895 | -1.51187 | -54.82179 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76686474-7202-3fb4-a0a1-f61379de1265 | -3.28629 | -54.01637 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b144ab74-b75c-3cdb-820d-1e8fb91f3282 | -3.01311 | -54.12741 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| a6061e0b-cb3f-350a-8395-227bbf31f835 | -3.8614 | -58.64894 | 2026-10-08 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acc859b9-9e83-3c56-8ab7-2b48fb265a02 | -2.77912 | -54.08044 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 012d9a23-8492-37e8-b457-f0014b6230e0 | -3.65925 | -54.28167 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99f0e288-36a0-3ee7-bd96-5d46408fb6eb | -3.17498 | -54.61232 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 374da065-1e5b-3e6f-95aa-05a54941ed62 | -8.72934 | -45.16564 | 2026-10-08 05:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 55d6b023-1cbc-3e3f-bdef-07fcc6990cc1 | -9.05099 | -65.92497 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78b74f37-b84a-3f6d-a4d0-09f3d547e5b2 | -5.03397 | -50.01775 | 2026-10-08 05:23:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 042d5af4-da53-3c72-a39b-5258d0dfdf07 | -3.94148 | -55.33105 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b10649a-7d0c-3b76-806e-166476e52740 | -2.51595 | -56.26152 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c0d616c-cc99-3772-817f-5cced4291694 | -3.27555 | -54.0388 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6dc10b2b-d51c-396f-95dc-114ea0aabb5e | -3.58104 | -55.60015 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1da36d31-20ff-3ad4-be12-ce740a146147 | -2.78783 | -54.09362 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c7a361e-1c42-3fb6-b24e-a8c44ef4dce2 | -4.56241 | -54.9549 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8558324e-6bad-3f1b-81f9-0b804b0a882f | -6.10306 | -55.72114 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf32b6a7-dc24-31c0-8e60-bdbd184a76a2 | -1.45086 | -55.2513 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5636c6c1-0fe4-3893-a79f-a53d29d401dd | -3.29256 | -54.04542 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4929f34b-abed-3d5b-a9b9-1390bea5159a | -3.95939 | -56.11892 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 36187230-49dd-33e1-8f87-25a1ce56d9e4 | -3.71829 | -59.33903 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ec518e6-39c7-3f7a-87a7-b22d7b26a563 | -3.05058 | -53.90959 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3aa32121-1e23-31cc-836c-6f62809cbe8d | -3.293 | -54.06549 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a105d3a-ab3b-34f8-8d5c-cf898b6dc46e | -3.99984 | -56.24637 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48d26c28-5646-3928-99b4-4e5a8d06c4b3 | -9.8062 | -65.00262 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e6c290d-6065-3eb1-a10e-1d8ee0a8a86c | -3.47153 | -54.69898 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b4c3cb7-64b8-38c7-ab3b-d51d835729c9 | -9.20034 | -66.08992 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1191937a-c006-335f-b15e-4e6170ccd035 | -5.70592 | -53.49518 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 76d888f5-f686-3c51-8662-df5cc044e041 | -2.84839 | -54.11879 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c841e66-abf8-3005-b1e8-a13818ce3aaf | -2.88057 | -54.07533 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README127.md)

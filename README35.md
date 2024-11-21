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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3cbb207-10ac-3ed5-8365-1995b89e69ce | -1.21428 | -51.79261 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d19b76c4-aefa-3941-a3c9-b7a5210e84c3 | -2.42202 | -46.51675 | 2024-11-21 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd2b7697-34e2-3778-b0f5-75398feb0b7c | -3.71633 | -49.4272 | 2024-11-21 04:29:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d24304d-d8be-3959-87e2-b17bfd78f922 | -0.94693 | -51.64239 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a83fa6fe-fdc5-3545-bc88-17ace9dfacdd | -1.58668 | -52.92978 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5776d2cb-7caf-3fd9-8336-51edf14947f1 | -2.69037 | -46.18589 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7dea7b16-400d-3203-8c01-543c0950cafb | -2.916 | -53.06807 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 76a5ad9a-ccfa-3c6d-87de-c4eac6a00e92 | -3.28978 | -50.53927 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59e5594d-1a8d-34dc-9aa8-91aada706b96 | -2.67769 | -46.16257 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e199ccc8-f565-3e33-a605-0f0786c446dc | -2.56083 | -48.17168 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1788e7d0-e948-38ac-85ed-15d4a914005c | -1.71208 | -52.48646 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 53f2ffa2-b51c-3cbf-be13-9fd97db36ca1 | -2.74957 | -52.10405 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a96cd61e-3a07-3787-ab32-4a8cd59b9cdd | -2.6395 | -46.21008 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5dbd8bd7-dc3e-32e3-83b1-5ca87d965687 | -2.83732 | -46.67365 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92405e87-1d89-3c21-88bd-5548e3463b73 | -2.65611 | -46.5566 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c84f03a5-7508-3007-9a77-035c1206a4e6 | -2.69778 | -46.24754 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64d993c1-017e-3d3a-a67b-0c59ff3f2ade | -1.20016 | -51.77536 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a7dd3a5-f5f5-3637-9ee8-06f64eeff0b9 | -2.51298 | -47.23018 | 2024-11-21 04:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eadb3e93-8f2c-3d7d-a6cd-dcdf8e6ce31f | -3.09423 | -53.21484 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 651ed2cc-e94d-3693-b2de-65105a5918a4 | -3.3308 | -50.4967 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d4a8c13-000f-32dd-81d5-3efeb0d9bc4b | -2.01677 | -52.01593 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c91e0c9e-8a5c-3855-a3ba-9572fa73a33f | -2.74134 | -48.64409 | 2024-11-21 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df7b1150-f6b7-3bd5-ab02-07e3badbe4a6 | -1.89789 | -53.33376 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b5baa7b-027b-3dd3-9288-0888fcd4bcad | -2.17583 | -46.38245 | 2024-11-21 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 55686dce-bc65-3b8c-a17b-677c367952c4 | -3.26386 | -50.61765 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff8581d8-3234-3b1b-aac9-7ef39e600707 | -2.84951 | -46.68262 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2b51e61-a869-3eca-ad18-f798a33fa971 | -2.36797 | -47.89014 | 2024-11-21 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7337123a-4d40-36dc-ad1d-585df419a383 | -4.04252 | -46.37065 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c4ac21d-cac7-3b1e-93fe-18c39d5c4f71 | 0.14346 | -51.08835 | 2024-11-21 04:29:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1853ee13-51ce-3a03-8bc4-0e177cd940d5 | -1.59009 | -50.4394 | 2024-11-21 04:29:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83d3859a-34c5-3d13-89bc-bdf500e02d86 | -1.54188 | -54.29039 | 2024-11-21 04:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf6d2047-492f-3114-b4d2-8a0de63ebe46 | -3.35912 | -50.18346 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2e1c932b-0bba-37de-84ba-540ede30b309 | -1.41588 | -52.81844 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8911c1ec-f1ce-3613-aa85-0c0fbe092404 | -3.7908 | -46.93576 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a348099-99b7-3010-909b-a6ecd641fa51 | -2.44536 | -48.92689 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9440f5e0-0d41-38b1-ba6b-6addfc0a7a3e | -3.26618 | -50.62706 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86a079e5-a1f9-3888-81c1-035240741b42 | -2.41726 | -49.10537 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf9c9934-0453-3412-a22c-9236998af2f7 | -2.56444 | -49.18194 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c1e7ea9-a617-3f87-bd7d-7cedd07abbcf | -2.16315 | -46.39817 | 2024-11-21 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6e09b564-e058-39fe-b110-d7645cbe6e2e | -3.29198 | -49.19491 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 2f525469-a0a1-3b33-a705-2764ee3fcc48 | -1.92479 | -46.60147 | 2024-11-21 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a64c86d-dadc-381c-b361-9e7793e1ada5 | -2.54407 | -46.21677 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0aa2b867-2632-3fca-90d6-3bdb9f069f69 | -1.98896 | -53.13898 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4bbeb596-5ddf-3b7c-9884-97a00f5e3b6b | -2.24386 | -46.85559 | 2024-11-21 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4fa2eb4-b7a5-37ee-bff8-41bfacc13b4f | -3.30064 | -50.36153 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f0a651b-5e2a-3ea0-8ac7-d3819ab9daf9 | -3.23004 | -43.26961 | 2024-11-21 04:29:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e73ed20e-e600-3f5d-8474-d723d806047e | -1.68631 | -50.19583 | 2024-11-21 04:29:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f47ea94b-12c2-3cf4-a583-a1973e15c690 | -1.34435 | -55.44402 | 2024-11-21 04:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2eaea41a-a959-3844-9b11-a8751981bb49 | -1.20699 | -51.97404 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b92e3a0-fd05-3c3b-a98d-7505ab9392b2 | -2.76886 | -52.11484 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4a660380-00ed-3c26-8155-74a1982fd992 | -4.13444 | -46.7092 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e82bf651-1e09-3872-b035-cc74708d2ea6 | -2.93685 | -48.33595 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 23bbec90-df1f-3508-acaa-8c0a994581f0 | -0.30383 | -51.569 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 330caf2e-b6a5-3015-a8d3-c247800a80a2 | -3.08776 | -45.96094 | 2024-11-21 04:29:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 826f229f-c337-31bb-9e62-f9765ac9218b | -2.35047 | -45.67733 | 2024-11-21 04:29:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa88f67a-432c-3f69-b8ae-3ca7f12426fe | -1.49127 | -49.6859 | 2024-11-21 04:29:00 | NPP-375D | SÃO SEBASTIÃO DA BOA VISTA | PARÁ | Brasil | 1507706 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7d80ddc-dc86-3080-b713-5d067c06a057 | -2.27 | -49.08239 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17a76f21-25f1-3859-8a08-2da3af3fa54f | -3.9258 | -46.48848 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25695419-49ce-3265-b8fe-d0f73647af57 | -2.20184 | -53.65504 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 587f7de8-5857-30ed-9a0d-d54bc3216906 | -0.98031 | -51.72205 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c601736-11aa-3512-8f6a-ca99973c6150 | -3.37067 | -50.72345 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8aced65a-7767-314a-9d4c-1bcb8b0db103 | -3.94353 | -46.71877 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d028b4f-5af0-3dea-822a-c5e8ecad3573 | -4.00444 | -43.25054 | 2024-11-21 04:29:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4810652-8b8e-3373-b78c-8681e588056a | -2.88693 | -49.4454 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 24e8591b-f421-37af-926c-9cf8403546a7 | -2.36948 | -53.83227 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0175560d-f9b4-3a96-b60f-2304fbc672b3 | -1.70845 | -52.48179 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c4901161-4699-3c63-bd05-867729e10323 | -1.83008 | -46.27903 | 2024-11-21 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eee09e5c-9020-357d-9027-324cf4563cb3 | -1.73168 | -52.39219 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 479495f8-a5ec-3a3a-82c8-6590289d0557 | -1.46533 | -52.6788 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57275a21-b25d-3f07-91b9-73e74f68d2af | -2.68864 | -46.07141 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7281af06-a13c-3ecf-b874-06b041d0207f | -1.42301 | -52.40674 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14deba88-7aa4-3e27-a480-132e95e56b52 | -2.62892 | -51.92706 | 2024-11-21 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ba5b8f0-bbf8-31fd-b291-21a83f1c752f | -1.49193 | -49.68177 | 2024-11-21 04:29:00 | NPP-375D | SÃO SEBASTIÃO DA BOA VISTA | PARÁ | Brasil | 1507706 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15380872-37a6-31e7-aa89-de35a72bae36 | -1.13832 | -53.66686 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 005725f8-93e2-3a3c-baf1-f3fd454ea0ac | -2.22088 | -46.39654 | 2024-11-21 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3de002e8-4050-32a2-ade7-02555b3fe840 | -1.01571 | -48.07225 | 2024-11-21 04:29:00 | NPP-375D | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37f224f8-a012-39c5-b366-4ac949215702 | -2.76581 | -45.1374 | 2024-11-21 04:29:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6eea9b16-e406-366a-977d-bc7d97166b85 | -2.41378 | -49.10481 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfe33de7-6f9f-3d75-ba00-b1fe5229aa2e | -2.69377 | -46.20778 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6daec05-c8cd-3e30-9ee3-f304c7b56f88 | -3.8813 | -46.66306 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37c5f5f8-cd6d-392a-a650-846ddecd50a1 | -2.22475 | -48.37742 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ea4b4ff-7ae9-3105-8486-1ff64ebc67d2 | -2.62033 | -51.92934 | 2024-11-21 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43a66c19-fd40-328d-8f48-99531df40c54 | -2.42588 | -46.51381 | 2024-11-21 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b4741e58-2bd8-3016-9179-1f53e1b9aa31 | -2.69669 | -46.25449 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f9900dc2-c480-336c-9014-1be5f40e2c03 | -1.62324 | -52.61398 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0b6c29c-c623-3364-a9c0-b268d9ec3378 | -1.392 | -55.18393 | 2024-11-21 04:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 320c63a5-410e-3e2f-ac95-7eb648ccdda2 | -3.10583 | -50.20292 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd99f36b-42aa-3372-8136-c7288f4f7f20 | -2.15431 | -50.46 | 2024-11-21 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9de6238e-15b4-34ce-abb1-0818d7a4fd79 | -2.8401 | -46.67762 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57997941-0057-39aa-8e96-c396cee66361 | -3.33519 | -50.49294 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f20d56b-3562-36cf-9da0-f85986fe9ea4 | -2.64174 | -46.21754 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aebdb01a-eda1-32c8-a221-e62c0b4d63a9 | -0.94276 | -51.71985 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e55bcdd-8874-3caa-b021-9f0c8ca9bf5e | -2.8349 | -54.01233 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 18adc545-1426-3edd-bbc9-6d07a825a1db | -1.52729 | -55.37678 | 2024-11-21 04:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56f61fe9-5b2f-39cd-9050-d68cd44214ad | -2.9547 | -53.71607 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0a75171-3874-357f-a503-196a7a821be1 | -2.20287 | -50.54099 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 927a421d-669c-3cfc-b1d0-6a269bc580b4 | -2.00082 | -46.61328 | 2024-11-21 04:29:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b944bd0-7195-3923-a1c4-5b358abb6ce5 | -3.19581 | -49.04135 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0468f2e-1573-3371-a119-584af807cae7 | -2.02018 | -54.53181 | 2024-11-21 04:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 2b808e72-adab-3d29-8897-4caa5b15243b | -0.88476 | -51.72221 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README36.md)

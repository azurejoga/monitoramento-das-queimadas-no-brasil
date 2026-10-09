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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2290a148-957a-3c0f-862e-9b28f5cd6df1 | -3.0925 | -53.9455 | 2026-10-09 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 4b0ad4eb-0adf-325f-91f7-513c27ed3cec | -3.5493 | -54.6951 | 2026-10-09 01:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 1ecbe223-a2d8-3897-9a43-9286a797b142 | -11.47 | -43.3824 | 2026-10-09 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 2d4d4ca2-6676-3bfd-86d7-bbdcd3768e6e | -10.6199 | -60.4852 | 2026-10-09 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 848a605d-e4c9-3728-bc12-2f6bac469e53 | -3.3455 | -50.4078 | 2026-10-09 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| c5ea6fcc-257a-3a6d-acc1-c7c0d8fff2ad | -6.1402 | -53.0574 | 2026-10-09 01:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 2d5a82b8-2e57-3209-b5e0-4103f96347b5 | -10.0616 | -36.4789 | 2026-10-09 01:50:00 | GOES-19 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 67.8 |
| b8868689-419a-3243-b04f-690b86d684d1 | -10.9953 | -45.4068 | 2026-10-09 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| d9f69544-7f8f-3fa2-9efc-669045916f1e | 4.4435 | -60.9657 | 2026-10-09 01:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 55.5 |
| c9cf9d2f-5f71-3246-a280-5970cd6a08ea | -5.9587 | -55.3448 | 2026-10-09 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| a32eff58-8121-3fd0-ab4f-48f1f3c82c01 | -7.1995 | -55.1627 | 2026-10-09 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 136.7 |
| 98925c2e-70a5-3620-8872-c43d21ea0289 | -13.1636 | -54.3591 | 2026-10-09 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 0e40c3e1-d641-32df-a957-0cf8635cab8e | -6.0019 | -40.9837 | 2026-10-09 01:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 601.0 |
| 9a48f1c1-9b3b-31df-bfe0-49f4b1bcb34a | -6.4903 | -62.8554 | 2026-10-09 01:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| d1494ed0-2207-3ab3-9482-9367579ebbee | -3.1787 | -50.5807 | 2026-10-09 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| c25d993e-d1bc-3d30-84cd-739585ca58f1 | -13.1639 | -54.3385 | 2026-10-09 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 93bdb388-f802-3659-aef3-1003f5f67098 | -5.7119 | -53.4658 | 2026-10-09 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 9ec54cd9-399d-32e4-ba1f-e745df171e74 | -6.0021 | -40.9594 | 2026-10-09 01:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 874.0 |
| 5bf021de-3211-3cf3-a245-2a1e2f998ef6 | -3.1971 | -50.5801 | 2026-10-09 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| c2054c39-08fa-3271-bb53-2c7f74910dee | -9.2781 | -47.4333 | 2026-10-09 01:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 9eb47c93-f0ed-3137-8230-1af3a92aea98 | -6.021 | -40.9577 | 2026-10-09 01:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 257.4 |
| 0cfe8899-28cb-3bd2-bdd4-666bb39d1692 | -13.1827 | -54.3571 | 2026-10-09 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 61a1f260-cb9f-336c-a7a4-b63c828a9c68 | -8.742 | -45.1563 | 2026-10-09 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 248.8 |
| f836f996-773a-3960-ae6d-7ab030d8f2f8 | -3.1786 | -50.6016 | 2026-10-09 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 8ba526c6-7c27-32c6-bd23-d065e418c768 | -7.2182 | -55.1416 | 2026-10-09 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 9300bf1d-9682-38ff-9b35-3def8ee08aba | -5.6932 | -53.487 | 2026-10-09 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 3a9ef1a8-867d-3242-9e22-73f6b92f7ed6 | -2.499 | -56.0675 | 2026-10-09 01:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| cd212dde-7c05-3e49-9fe9-5643950f5679 | -3.364 | -50.4072 | 2026-10-09 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| d6937aee-0606-36a6-a9d9-e614c865d9e1 | -12.0058 | -43.464 | 2026-10-09 01:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| ff6654e3-2389-34d6-a8f5-b74643dad4ed | -8.5051 | -54.6202 | 2026-10-09 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| ea2732e0-702c-379a-85c3-52dfc64d11e9 | -13.1668 | -43.2673 | 2026-10-09 01:50:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 81.1 |
| a9acc021-6c92-3089-a574-0e006f1e19a1 | -8.4865 | -54.6215 | 2026-10-09 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 92d833ad-ae2f-36b0-8b15-e313f2345395 | -7.1994 | -55.1827 | 2026-10-09 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 5b49de5b-8bf6-3a2d-bc94-fb0340a84aef | -8.7426 | -45.1106 | 2026-10-09 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 66d17ae5-3ce5-3bfd-a5ce-892aa74f7a10 | -3.1879 | -58.6433 | 2026-10-09 01:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 4c923c4a-9350-33ef-94e7-3e166969abed | -3.1787 | -50.5807 | 2026-10-09 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 351e567f-f9a3-309c-8a96-ee6069c0c9c9 | -8.911 | -45.229 | 2026-10-09 02:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 8f5b0419-c5fb-3ac1-85e1-f96cb24eeddd | -3.0925 | -53.9455 | 2026-10-09 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 4d747cf7-863d-3979-b54a-cef32cc2435d | -4.6282 | -49.2147 | 2026-10-09 02:00:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 2f7c370c-b7f6-3f57-8e96-f403cf02219a | -3.1879 | -58.6433 | 2026-10-09 02:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| f71c62e4-4d30-3522-854f-f52c8af2de8a | -6.7363 | -55.1675 | 2026-10-09 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 38f0f1c7-df34-3062-8071-d141ee08b450 | -6.0019 | -40.9837 | 2026-10-09 02:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 282.0 |
| 4fd14695-488e-396f-bf9c-546fd0ec821f | -6.0024 | -40.935 | 2026-10-09 02:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 106.7 |
| 95ba4ff7-1afa-357f-ade4-d987ba4676cf | -6.021 | -40.9577 | 2026-10-09 02:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 151.0 |
| dd045ef3-aa85-330b-b495-fe4c1ee77121 | -5.7117 | -53.4862 | 2026-10-09 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 423b985d-3692-36f1-a605-39d0658daea1 | -6.8719 | -45.9003 | 2026-10-09 02:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 72d4d60b-5488-3df9-9cd1-b4a0cae5534e | -5.6934 | -53.4667 | 2026-10-09 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| c8d7caa1-0602-367b-9fe1-9b26d6e68dae | -3.1971 | -50.5801 | 2026-10-09 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 1538f5ae-d072-34d8-b33b-2151779b5224 | -3.1101 | -54.1661 | 2026-10-09 02:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| f3bbbe1e-21bb-3dfe-9b97-5c03e59b8e2e | -6.0021 | -40.9594 | 2026-10-09 02:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 441.1 |
| 498bb3dd-1828-39b7-a834-f9a99a48c125 | -13.1827 | -54.3571 | 2026-10-09 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 8f5679d6-8bb8-3ee6-ae11-cee7085db73b | -7.5649 | -61.5523 | 2026-10-09 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 2f1a8861-eb5f-387a-9df2-d4c87a95f0dd | -7.1995 | -55.1627 | 2026-10-09 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 04547e2c-5591-3d54-b5bc-c60fae4acdbc | -3.9912 | -59.356 | 2026-10-09 02:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 06bfca67-5ff2-384f-acba-710a11a887fa | -3.3455 | -50.4078 | 2026-10-09 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 8d9debd8-f5b8-3130-83bd-dbe9cb1e4733 | -7.2182 | -55.1416 | 2026-10-09 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 78959520-b0db-3853-8383-bfd9e2395f79 | -13.1636 | -54.3591 | 2026-10-09 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 0b9cc30b-b984-3c2f-8d27-fd321627a6b4 | -11.6562 | -43.6846 | 2026-10-09 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 688a7728-6d4b-3a31-b2da-2f16124651a9 | -9.4769 | -40.3365 | 2026-10-09 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 61.0 |
| b45597f8-135d-3803-a543-16185ed446db | -5.7119 | -53.4658 | 2026-10-09 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 304649ff-d9a1-3327-b937-64b27aa662fe | -10.6199 | -60.4852 | 2026-10-09 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 33034ba0-f3a2-3fea-a5ae-64529ff0e60b | -10.6012 | -60.4863 | 2026-10-09 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 37.8 |
| bbd0675c-4792-3511-91c8-fb656a1eb457 | -7.2187 | -55.0815 | 2026-10-09 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| e49b04f1-b5bc-36e9-8e5e-45f233c3e929 | -11.6173 | -43.7142 | 2026-10-09 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| d88fc1e4-f9cb-378e-b557-f77d5c4f6cdc | -3.1285 | -54.1657 | 2026-10-09 02:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 130.1 |
| e89b9b78-44d3-33e2-8002-2ae68fb34cb7 | -3.2576 | -54.0418 | 2026-10-09 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| a0c9220a-8692-313e-92e0-cb3cb27097bf | -2.499 | -56.0675 | 2026-10-09 02:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 65e5bf6e-d4d0-324e-a7d9-63230d092ca2 | -12.0058 | -43.464 | 2026-10-09 02:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 278a59ef-2f56-33e0-a912-23a3f7749e9c | -6.8907 | -45.8988 | 2026-10-09 02:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| ffed0ad0-8b3b-369c-998f-61e7ecabec3d | -3.1114 | -53.7839 | 2026-10-09 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 71bd7666-33b8-3876-87f9-9fea7078228d | -8.7426 | -45.1106 | 2026-10-09 02:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 505791d6-7204-361d-a488-9965456d62a7 | -9.4578 | -40.3392 | 2026-10-09 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 72.7 |
| 3527cff1-328a-3df1-adc1-8ce41e37abbe | -3.5677 | -54.6746 | 2026-10-09 02:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 52c47eba-cb2c-33c6-81b4-917f52722a3d | -3.5493 | -54.6951 | 2026-10-09 02:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 122.7 |
| a5a38ec5-5ac6-3a47-ba58-79bfa5b17d0c | -5.6932 | -53.487 | 2026-10-09 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 63329cff-9823-3021-bfc6-86fe4b501caa | -3.5676 | -54.6946 | 2026-10-09 02:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 5e5f57cc-17db-33db-881a-c0ad22f55fd3 | -6.4903 | -62.8554 | 2026-10-09 02:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 9a06a55c-7a60-3f72-a4cf-c64246686d9d | -8.742 | -45.1563 | 2026-10-09 02:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 252.4 |
| bdaa8814-aaec-34ad-b928-7d83a46804eb | -3.5493 | -54.6752 | 2026-10-09 02:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| b65b70a4-7bc6-3d62-8354-258461ca3940 | -3.1109 | -53.945 | 2026-10-09 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| aa3a4437-4731-3659-a123-27192d890fed | -2.7428 | -54.1146 | 2026-10-09 02:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| d2247aae-1cff-3d42-a1fe-d064971c9e79 | -3.1284 | -54.1857 | 2026-10-09 02:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 52857730-d8b8-36a3-81c2-142301130579 | -3.11 | -54.1862 | 2026-10-09 02:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 9e29a9bd-bc20-3007-b9f0-da58252b6b89 | -9.2549 | -60.8863 | 2026-10-09 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 579bd496-bf33-3f44-bcf8-52a429fc8ce2 | -13.1639 | -54.3385 | 2026-10-09 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 712d0baa-cd86-33a2-b356-5876453fd072 | -6.0207 | -40.982 | 2026-10-09 02:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 131.4 |
| bb022235-2f34-387f-bdac-1b7448d60d2c | -10.9953 | -45.4068 | 2026-10-09 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 451c78c3-8374-3f47-aea6-00c253ba0f4f | -8.7231 | -45.1583 | 2026-10-09 02:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 09eed222-bece-3246-900c-1f73f030fcd6 | -3.364 | -50.4072 | 2026-10-09 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 2bb9bc30-b78a-3c1d-a553-11a271dc2869 | -8.7234 | -45.1355 | 2026-10-09 02:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 180.1 |
| 31f3f9bf-edb7-3884-a3da-839e2ccd3e0c | -7.218 | -55.1617 | 2026-10-09 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| fb644935-53af-39fc-8770-ed38e1cafa24 | -8.9687 | -45.1542 | 2026-10-09 02:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 2f1dc51e-d6a4-35af-bb46-91d6da631cc5 | -6.7365 | -55.1474 | 2026-10-09 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| b28336b1-f106-3376-8beb-bf7fe3cfee00 | -8.7423 | -45.1334 | 2026-10-09 02:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 428.9 |
| 68ffea67-f752-3116-a135-fe9989916f72 | -3.0007 | -53.9075 | 2026-10-09 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 5b6ecd19-8d97-329a-9763-950d71d0b27e | -3.4396 | -54.5382 | 2026-10-09 02:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| ccbcfb93-43e7-3035-a07b-d496e00752a4 | -9.2781 | -47.4333 | 2026-10-09 02:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 22fd7e16-4c8b-3080-b3e9-98e32612f030 | -3.11 | -54.1862 | 2026-10-09 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| d0b13e41-a508-3e32-895d-ca8af51c15fb | -5.9833 | -40.961 | 2026-10-09 02:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 62.7 |
| 7a1ff79b-28b7-37d9-badb-b41f6356d215 | -3.5493 | -54.6752 | 2026-10-09 02:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |


[Clique aqui para ver as próximas entradas](README51.md)

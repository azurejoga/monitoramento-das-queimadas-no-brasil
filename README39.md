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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8dd2b97-e751-3eb6-94b6-1a31e053491d | -4.28727 | -50.77211 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 869bbd1c-8751-381c-9fcf-ff8bef643450 | -7.40757 | -55.59952 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f9312deb-7551-3090-98f9-b4947b886d4e | -7.48618 | -55.00048 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 94e9ae7f-b065-3bb8-8cec-6ef2045e1307 | -4.27755 | -50.76308 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04c2f429-c18c-3321-93eb-7d03cd9d3c4a | -7.83546 | -55.14527 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a4f8fe4-a195-3482-b306-2de545ede6f2 | -5.75084 | -45.14835 | 2026-10-02 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c1f06d9c-3b55-32ba-b23e-31e029f866eb | -3.9351 | -49.00451 | 2026-10-02 04:14:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9c604c2-b590-3f3e-a820-31dd361d1446 | -3.28441 | -53.86281 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 81e23c7b-ebe6-363b-bbe3-f1b8dd506d09 | -7.40907 | -55.59159 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 599e263f-5ae9-36ce-a533-b638f595a23c | -3.99555 | -48.40106 | 2026-10-02 04:14:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af8df4b1-d99f-3f0e-8606-1163dccef80e | -6.33989 | -43.37649 | 2026-10-02 04:14:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a4abdbe-b479-39c7-8db4-a03ea1e55a49 | -6.27297 | -43.26831 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b11e23b5-8f45-3d7d-813d-2b4e942711cb | -4.25626 | -50.75593 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bccf6019-ec55-3254-9ff2-243c6b9b6be2 | -5.75893 | -45.14525 | 2026-10-02 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b0b78715-c470-3a6a-8971-c49adb528331 | -9.32783 | -47.25233 | 2026-10-02 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1cb11f95-ba21-3daf-a465-c9a7e1516dcc | -6.75111 | -55.08433 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 142ca1ae-a0b2-335f-aa6e-4457c2ac95ce | -6.33463 | -43.36059 | 2026-10-02 04:14:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f915c6a5-20d1-35a9-8141-85fdc1cbc83e | -7.82589 | -55.13023 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5db9ce01-1875-3371-a38c-cab74bd55443 | -4.2453 | -50.74998 | 2026-10-02 04:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e01f1263-0a70-3ebb-bdac-559ab42996a7 | -6.43156 | -55.81149 | 2026-10-02 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 373aa913-3bb0-3c2d-ba41-77cbf35499d3 | -7.65193 | -55.10481 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e75a04f-a237-301a-affa-39f6e4a11b3a | -6.24611 | -53.1395 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c9b3f60-c592-3fcd-a78c-f5c3778c9123 | -7.88249 | -44.17811 | 2026-10-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65ce2919-210e-3266-9b8b-3a1cd9dfb17f | -5.73312 | -43.2878 | 2026-10-02 04:14:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5758d0ed-9489-3456-8ec4-9446e27986bf | -9.33575 | -47.25387 | 2026-10-02 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee99a7fd-9346-3c7c-adfd-e2767cecefdb | -6.90105 | -43.69934 | 2026-10-02 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 019932d8-80b0-3897-99ba-e45425887630 | -7.4978 | -42.82012 | 2026-10-02 04:14:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 4197e281-4235-3766-9777-79bf4f6741c1 | -6.2475 | -43.77267 | 2026-10-02 04:14:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 4f4d9bce-2a89-3174-a2fa-74e66215c2c6 | -7.45733 | -54.99556 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df6be6f9-e7a0-3e09-b82d-505755b2cb5b | -7.46579 | -54.99733 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 397b87c9-ca58-38f1-8033-6e907c46cbc1 | -2.89328 | -54.15135 | 2026-10-02 04:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3706fd3b-37cd-34fc-81a5-4237aea5c888 | -8.01024 | -47.43277 | 2026-10-02 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 69f81352-8136-37c8-82b6-0c7dc2753b37 | -9.83098 | -44.85318 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e64bf98c-dfe7-3725-9541-89bcd3b91f92 | -4.06152 | -51.12369 | 2026-10-02 04:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92641e3c-48d5-3540-89a3-2d9ff7bd04ed | -6.18659 | -44.08389 | 2026-10-02 04:14:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3cdb46c2-06fa-3590-b689-f542f6d83b22 | -6.09414 | -47.67608 | 2026-10-02 04:14:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 850a9ae2-f58c-30f6-aa47-f28b38d732f4 | -4.26476 | -50.77193 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6426050-a0c3-3cfb-be13-5b61be4d424b | -7.33793 | -55.58458 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a325c168-ae6e-307d-955b-2b998e47a835 | -4.26348 | -50.77934 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ecff425-d40a-3b9b-a240-2b8c094f3769 | -3.18365 | -54.11044 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 51128165-19d9-3123-bc2b-a0558da3c3fd | -3.74987 | -40.55519 | 2026-10-02 04:14:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 46d63219-e93d-3073-beb0-aa8aed9fdb5d | -8.91529 | -49.26087 | 2026-10-02 04:14:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 788480a0-3c6e-3f55-99a5-3978165f67ab | -4.25872 | -50.7418 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 218d23fc-6b2d-30c6-8c9c-a2297ed1576d | -6.89883 | -43.69138 | 2026-10-02 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a13995b-fadd-3963-9e05-ef0a97b8a452 | -9.19579 | -41.77395 | 2026-10-02 04:14:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 3738ae14-4a5a-34b8-b74e-1c659adbf634 | -3.39159 | -44.75075 | 2026-10-02 04:14:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2b68353-5ed4-3ce6-b4cd-6cfa69e93629 | -6.14791 | -52.81134 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e268bc09-8ce1-3e48-97a9-8674fec0d68e | -6.31322 | -43.34214 | 2026-10-02 04:14:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6ad0645-a9f2-3ebb-a35b-39d47c893be9 | -8.74755 | -47.59042 | 2026-10-02 04:14:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0dd46a6e-1e41-3c96-801d-c68d801ebed1 | -9.79386 | -44.80764 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5e71022e-4881-328c-a359-a12975d6edb7 | -6.42974 | -46.67752 | 2026-10-02 04:14:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1dd1d38d-959e-339f-b817-31f37f5799ac | -9.21376 | -42.15616 | 2026-10-02 04:14:00 | NOAA-20 | CORONEL JOSÉ DIAS | PIAUÍ | Brasil | 2202851 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| cd05b250-a936-3818-996f-c3d619b7670b | -7.83785 | -55.13262 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8e195f03-0626-3158-9df7-2f3179425b9b | -8.02735 | -47.48162 | 2026-10-02 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b970077-744f-3af5-918b-800d8b5e2909 | -6.23293 | -53.14195 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3d60cb87-5221-31e7-bb1a-bdf3436fa9b7 | -7.86525 | -44.17533 | 2026-10-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a7b766fe-969a-3404-9405-15f5b271617e | -8.96631 | -46.82518 | 2026-10-02 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09df652e-8b64-3579-9aa6-6abd077f1f06 | -7.19444 | -52.6137 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 94283feb-fca8-326b-ae96-fc8a213a2b47 | -3.27763 | -53.84741 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 289b43ee-ce52-3d3a-885e-463025913ece | -7.52177 | -50.53518 | 2026-10-02 04:14:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8b790a9-243d-343e-9954-9f21fff3d210 | -5.99309 | -53.54647 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 498a9024-76f3-3eeb-867f-3827e7837916 | -8.35356 | -45.03576 | 2026-10-02 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2886d178-2dea-322c-bf44-b0f1de79ae6c | -8.97823 | -48.93948 | 2026-10-02 04:14:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93a0c6da-ea71-3856-bfda-eb6d0113184a | -5.86932 | -43.59347 | 2026-10-02 04:14:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4464a5e1-cb26-37cf-a831-f8d84bd52134 | -8.07694 | -54.88967 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 79516c06-6667-3a22-a004-3cdb243af7ea | -5.75964 | -45.14094 | 2026-10-02 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e0c3af57-6027-31f9-8342-9bd0d83bd40a | -4.2976 | -50.77762 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 541331b4-d0b0-3762-a979-17cd330dd023 | -3.28439 | -53.84843 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 25bd4e11-7573-3b9f-b8b7-ea179cea753d | -9.58686 | -45.50887 | 2026-10-02 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d90f67f5-13e7-3f45-9351-93ebadacec9b | -6.17476 | -53.18072 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3b75d99-0c46-3c77-af79-131e808bb088 | -5.86244 | -53.48334 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 548cea02-80cb-32e7-8bf4-04e579bd244c | -3.1408 | -53.74237 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a3ca1cff-9d21-3a6d-b47c-ced7ff6e8195 | -6.19185 | -52.81018 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c5ccfa26-73cd-31ec-acf4-251e93fc6a31 | -7.33996 | -55.58566 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3293a0e5-b7aa-39b9-988b-ade582896553 | -6.44163 | -51.70754 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb1475bd-27fa-32b2-af93-751367c0c132 | -7.38992 | -55.20719 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| fbbf9227-b37d-33a7-b451-b1f5c92190b3 | -9.82289 | -44.8159 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 09a9d3d8-5b17-3728-adf7-a6dee488faea | -9.82815 | -44.84872 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2857287d-8004-3d5c-b04b-b6029a508b88 | -4.06537 | -51.1161 | 2026-10-02 04:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec8b62ce-4351-383c-9e88-0a3cd58bb3c1 | -4.44805 | -54.90593 | 2026-10-02 04:14:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a969ceed-b48c-384e-a19c-a624b7e3523c | -9.52598 | -45.33386 | 2026-10-02 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9ac8870d-0993-3a38-8e09-1562194cdaf6 | -4.45535 | -47.91899 | 2026-10-02 04:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 7134bd6a-999f-37ba-aa81-a80d48e17ebd | -2.8999 | -54.15227 | 2026-10-02 04:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 951b2edd-d202-3d91-8bb5-578143fd7efd | -4.35724 | -47.77621 | 2026-10-02 04:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 56101457-c5e7-3e96-81d7-ffc233c3ebc9 | -6.91652 | -44.56403 | 2026-10-02 04:14:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4df554a2-7a23-3f85-9733-8f5c601c3071 | -7.33428 | -55.6033 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 560e91c7-9327-3294-a747-be8ec60d02d3 | -5.47198 | -38.24081 | 2026-10-02 04:14:00 | NOAA-20 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 442b1650-0de5-37b3-ae57-14da052994e3 | -3.9847 | -41.5176 | 2026-10-02 04:14:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 411d161b-ea07-32ba-947a-2939061c9e61 | -8.17391 | -54.79816 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dea44443-4ade-3d76-b9f6-c632db26b2fc | -9.81901 | -44.83923 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65df8c7a-c18e-34d5-a3f7-a981dbc6c4e3 | -5.75973 | -45.1634 | 2026-10-02 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c8a8a0bc-e40f-3b90-8536-f342bd28ed30 | -5.27341 | -42.63842 | 2026-10-02 04:14:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e53b6c95-ae19-36d5-ae33-e9d2ab3ad216 | -3.28337 | -53.85443 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| bb1ddea6-82f1-31aa-b992-3c4f0fe01768 | -5.75821 | -45.1496 | 2026-10-02 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 93d4ae44-b2fc-3a36-9071-f04448f713ab | -6.00413 | -53.54638 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af230968-7b6e-3617-b9fb-d877c53d5d32 | -4.28241 | -50.76761 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d55f08d-15bd-366e-b22f-8b8b46d7b8e9 | -7.87967 | -44.17374 | 2026-10-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 270ded7b-5b9a-3909-a075-b2390d34e2d3 | -9.90034 | -44.93919 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20627f98-3cf2-39b2-9b44-a7061c9175f0 | -6.89361 | -43.70195 | 2026-10-02 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e9ace46-e7a7-3667-881c-fb70b19b2590 | -5.36511 | -46.73182 | 2026-10-02 04:14:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README40.md)

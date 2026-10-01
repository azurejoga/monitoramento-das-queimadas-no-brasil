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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4066902a-1068-39c9-a46f-40fa19218e5b | -7.03767 | -50.72877 | 2026-10-01 04:34:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| da3fc03e-1fde-3845-8823-041cb384e4f6 | -7.63425 | -55.06211 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 31bfc0a9-f3e0-3834-91c3-8e3efb98b22c | -6.92052 | -59.29422 | 2026-10-01 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0aa46a08-f7a9-3ee7-aefe-1d8aca4dc1e8 | -6.4368 | -55.80528 | 2026-10-01 04:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cccf531-c09f-39e9-88d2-3a250cec76a2 | -8.17641 | -54.79338 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7442c006-e33a-31c6-b22e-eab0976b70c5 | -9.44344 | -48.86203 | 2026-10-01 04:34:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6b4442e2-5289-3706-8d08-93a64cd7e5a0 | -9.81274 | -44.84317 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ec76dfe-1ee6-31f2-800f-f52c04ac57f7 | -10.86603 | -54.10156 | 2026-10-01 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6186570-deca-3fee-981f-cac2538543ef | -11.79949 | -50.51785 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9abdcfd-9c3a-36f0-a3d7-7b0d76ca5662 | -10.81618 | -48.75357 | 2026-10-01 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50db5820-90b2-331a-8818-2621ca944d82 | -11.17444 | -45.11345 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5394907-6d42-3216-8e33-27b4f1406734 | -11.21963 | -45.16864 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 751d1814-d8c0-339e-acf9-0e58d56a16ef | -11.45505 | -43.43009 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 93efe955-dc70-3262-bad1-ffacd78ec9f2 | -10.85415 | -48.68963 | 2026-10-01 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00b928f6-0d31-34ba-84ae-70fb95cc706a | -8.32951 | -44.15884 | 2026-10-01 04:34:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9359bb2b-21ba-3de7-8a2d-a3df6486f1ba | -10.90504 | -43.84641 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8acc5e9f-24db-398f-aadc-9544ecb908f3 | -11.79622 | -50.51815 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 887b47ff-fb4e-34a2-a448-dca64c8e28b7 | -7.56815 | -47.20935 | 2026-10-01 04:34:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4733f4e-a6c7-379a-9def-d09dfd51e4cd | -11.20229 | -45.14189 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 473f44aa-3144-3848-a7a5-bf83b5a3dde0 | -10.46029 | -46.76889 | 2026-10-01 04:34:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7dc92999-5f0c-3c4d-8daa-6f00d1985515 | -6.13738 | -53.06678 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb448304-27ce-3976-b4fb-dea2b020e347 | -8.2016 | -45.491 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8bcc0f4-098e-31f8-8a68-9b862d1dfdf7 | -9.7087 | -47.76286 | 2026-10-01 04:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29be3433-77a7-3766-a89f-0b76ba269cbe | -11.71293 | -43.43881 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44d4ce7b-b37b-32dc-b582-2ce920d2700e | -10.2386 | -44.60639 | 2026-10-01 04:34:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5154348e-b953-3ffa-b799-e42beb40a71c | -11.25509 | -43.53106 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 49060116-ce6c-36c1-8a0b-7307779065bb | -10.29742 | -44.64697 | 2026-10-01 04:34:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd4ac5bf-324b-34f3-b628-7817096f5731 | -13.33971 | -46.82584 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13988926-2f91-3f8b-b814-68a391834310 | -7.55194 | -55.03061 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a012bb1c-0021-3037-bc39-26b53620ceae | -12.09415 | -50.68922 | 2026-10-01 04:34:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 065c7440-cc04-36bb-bed8-eb2c5559ce40 | -11.38004 | -43.36274 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 982a2e53-52fa-37d7-ac5f-3703d24e6793 | -9.06554 | -49.86724 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9fcf8bb-2056-3efa-84a9-d3abbc3ed502 | -11.79117 | -50.50472 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 10a50eeb-debd-3404-984c-60b299390cd9 | -11.73477 | -50.40749 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3228e279-5aac-39d1-8b35-320ee9cc7503 | -12.45249 | -44.19169 | 2026-10-01 04:34:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0c05c61d-04ab-3016-a486-e0cb6edca490 | -8.33243 | -44.16338 | 2026-10-01 04:34:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ef28e5c0-345e-3223-ad44-cd212d5dbeb4 | -9.07643 | -47.16685 | 2026-10-01 04:34:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a97a2690-a67b-3944-a6db-c1063252de4a | -10.76036 | -52.12946 | 2026-10-01 04:34:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 216b1086-ea37-3c43-9dce-9721cc242a15 | -9.20856 | -45.82318 | 2026-10-01 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3da5e11-6103-3c94-bfe7-dd4b13e823e7 | -10.83904 | -48.69786 | 2026-10-01 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74f2f8c2-b40a-3c75-bff4-087533b8956e | -5.86163 | -57.75581 | 2026-10-01 04:34:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54c58292-86e9-3d6c-9d72-dcb2ffabc27c | -10.91615 | -43.84797 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f14cc695-f926-3f6b-b113-c3fc229fffac | -6.51358 | -55.88671 | 2026-10-01 04:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f517f32-a1cb-39df-87c2-f632497a659c | -12.03537 | -51.01913 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8bcab1c1-d3cd-37ef-89cf-810c3c976546 | -8.84077 | -49.69117 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e57d61b8-0e1b-3dd4-8a29-08add77e4ea3 | -7.19063 | -46.50542 | 2026-10-01 04:34:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6145956-8d07-34ff-b04b-14a4ef28c65c | -7.55642 | -55.03446 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcd54911-0ae5-36f1-a2e5-7f89df2b272f | -12.50575 | -43.10078 | 2026-10-01 04:34:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 895f6836-7416-3b5d-b6b4-cd09de000267 | -8.23719 | -54.77851 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3ecf536-5093-39cb-b1c3-58158ff5fec1 | -13.53668 | -49.16836 | 2026-10-01 04:34:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf99824d-7134-3176-9956-09faa02ef072 | -8.01519 | -47.45282 | 2026-10-01 04:34:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9857bd8-5ee2-3274-833b-21c6476e0514 | -11.61818 | -43.55573 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 67de22a7-361d-31f6-be45-b82a50d26b4f | -11.16744 | -54.11702 | 2026-10-01 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fcb7597a-81e9-3180-a975-9190a5025624 | -11.25956 | -43.52694 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ada3842e-b694-3a1b-a751-a193357e553a | -13.87141 | -43.99339 | 2026-10-01 04:34:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 670c71ce-bd10-3472-99ca-ffaf7a9487bb | -12.85977 | -44.34019 | 2026-10-01 04:34:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 656e0e96-408b-3b01-9425-21c9969b0133 | -13.17213 | -48.51908 | 2026-10-01 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e67b43a4-c3b5-38f4-a9b0-46943b01ac8c | -6.35048 | -55.33772 | 2026-10-01 04:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82bd5ef8-035e-3c7b-a790-f9f27f256ca4 | -13.51316 | -46.88605 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a7e5fe3-5e9d-34bb-9f0f-01382ed5bf0e | -10.75637 | -50.50975 | 2026-10-01 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| dfa1770f-6a74-355a-a4d7-ffe999d47ef9 | -10.28387 | -53.97148 | 2026-10-01 04:34:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 41b25d85-3e21-3fbb-b12d-8e9c9f10dcbc | -13.25834 | -42.46535 | 2026-10-01 04:34:00 | NOAA-20 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f5e85d60-8997-3774-85a8-4eff29b71690 | -12.37064 | -51.14676 | 2026-10-01 04:34:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5370f60-5303-3f87-b377-d252fdbed546 | -11.65302 | -43.55609 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a62d3a4-52e1-3bc7-8c90-fc0aacaa7d21 | -7.34689 | -55.5934 | 2026-10-01 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cedbcebb-b0d6-3812-97ca-173f26f1aa1a | -12.20775 | -43.83396 | 2026-10-01 04:34:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ed95480-1fbb-3c24-a9af-8abb72dabf6a | -7.02234 | -47.54138 | 2026-10-01 04:34:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 864fbff2-0f0b-3ee6-a52b-40bdd137dcab | -8.13687 | -43.43357 | 2026-10-01 04:34:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da6d9813-bed9-3f4b-a596-5a283b3648c3 | -9.7771 | -44.81063 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6dedd466-448c-354d-864a-6a6037bada81 | -10.50763 | -50.84902 | 2026-10-01 04:34:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 571da01f-a923-3530-b209-1b6f94edb413 | -12.38077 | -51.15298 | 2026-10-01 04:34:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96e74cbb-041e-36e1-9aa4-814d06cf970d | -7.63373 | -55.06506 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91d25384-68d6-35a9-9666-b46c831f1f19 | -11.82497 | -49.51262 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b9325a1-9379-3a57-8492-e760c4622433 | -11.42343 | -43.40596 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 39a9a46c-91d1-3e6f-8b6b-3677d31d3c3f | -8.38574 | -46.29263 | 2026-10-01 04:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2393564f-6ec2-39d1-8c24-3e422452cd9f | -13.38467 | -44.02373 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f63a9cc-95b8-3568-842c-b31d88c96db2 | -13.53392 | -49.16428 | 2026-10-01 04:34:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d26ef5f8-4f7f-3ce2-b9e3-777ac4198cda | -8.50874 | -45.54527 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ecde1c64-9950-37ce-9681-520f56ea71e1 | -11.29926 | -54.8798 | 2026-10-01 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f123543-68da-3b01-ab0e-c4f2dc96801f | -12.22944 | -50.33373 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2dc37c25-f532-37c1-8ce6-6f05dd6fe48b | -7.72375 | -54.79067 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4562b427-b9f0-32cc-bdbc-5b1cf36bf542 | -7.7235 | -49.54403 | 2026-10-01 04:34:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53e4a090-e181-3e20-aec3-f559b58ef09c | -10.08239 | -50.33915 | 2026-10-01 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd437ec1-499a-3f0a-8af1-c9b32fba7f66 | -7.60322 | -55.69915 | 2026-10-01 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c157944d-fb27-3394-a3f1-f3afd49c10a6 | -11.17185 | -54.11789 | 2026-10-01 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c20ce45-6861-3885-bd99-ab520ac70583 | -11.17114 | -54.1163 | 2026-10-01 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fd54c3ea-88e0-3989-92fe-6330dcc43d81 | -11.21157 | -45.15127 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5886b69f-e4be-3575-a381-3b7d397cd50b | -13.06306 | -51.19936 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52008ff0-2285-324a-b178-f74ddef891bb | -9.21479 | -50.68709 | 2026-10-01 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47c491d0-5d07-3ee4-ae2f-afde55624f15 | -9.21553 | -50.68272 | 2026-10-01 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 009f836f-9b54-3c12-901b-5d3a138f19de | -13.14869 | -48.55912 | 2026-10-01 04:34:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 165b013e-1d41-34a5-a2c4-9405bc01ce81 | -11.65681 | -43.55665 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7585976e-3bad-339a-9be4-1034f1303b94 | -7.56483 | -47.20882 | 2026-10-01 04:34:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7fd7df6-c85f-3bc9-9259-7d84160e4264 | -10.2951 | -44.63835 | 2026-10-01 04:34:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e5de820-1422-3a8e-bce7-8ddc03ac6166 | -9.75381 | -44.82293 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18437714-6db5-343b-b14c-9a2b4621db6a | -6.07834 | -53.30615 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 52f86cb8-f0ff-353c-8442-0d09940ec2f9 | -8.84231 | -49.70371 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5d8d8ee5-d93f-3d95-a7ad-d3c0d151cd5b | -12.71009 | -54.06403 | 2026-10-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45785cec-58bc-3629-ae48-4144a7b5d40f | -10.84788 | -48.70705 | 2026-10-01 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3fd43324-a7f0-360f-8b1d-5eb9c0a85558 | -11.4342 | -43.41245 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README65.md)

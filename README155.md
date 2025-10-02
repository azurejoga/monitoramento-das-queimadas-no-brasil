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

## Dados Diários - Página 155

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c9a79fe-4268-35ea-8cd0-bbd6b04ee6ca | -9.3364 | -45.9079 | 2025-10-02 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 11f72e5a-a7f1-3ac3-bae1-58443d913c12 | -7.0306 | -43.3444 | 2025-10-02 13:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 84.5 |
| 282d0d2d-0635-3b1d-9871-c46f329ded7e | -6.7624 | -45.617 | 2025-10-02 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 8ba759e0-47a6-3894-a98f-f8f89978933b | -14.1921 | -46.1321 | 2025-10-02 13:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 152.8 |
| cfc2b282-f33b-3399-a10e-937e0a162e3f | -9.4086 | -47.5521 | 2025-10-02 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 120.6 |
| d153f707-e342-3e67-9e9d-ab8c4f1d6a5b | -10.1837 | -50.3128 | 2025-10-02 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 25acc03f-a466-3fa3-b9db-ecad89e03e80 | -16.0417 | -50.8959 | 2025-10-02 13:30:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 4ca89727-e7e9-38c1-929c-11856f1da508 | -6.0997 | -42.4865 | 2025-10-02 13:30:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 78.2 |
| 1ced90e8-d94c-3d1b-bd94-362524148d75 | -13.3131 | -47.5876 | 2025-10-02 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 0fd13b0a-22d4-3927-9cfd-452dc570c3e2 | -14.425 | -46.1381 | 2025-10-02 13:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 4d76707c-826b-33b4-98f5-435b36e30172 | -8.8929 | -46.6072 | 2025-10-02 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 86e933e1-a964-331b-b676-eaff7d9b2ca0 | -6.2328 | -44.2257 | 2025-10-02 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| d5a40aa1-7c0a-384c-9498-82a410b5c2ae | -8.6534 | -47.6943 | 2025-10-02 13:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 7bb55ce9-fdae-3308-963a-a457eab466f1 | -6.6978 | -42.8118 | 2025-10-02 13:30:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 113.7 |
| 30fb2364-f442-3a42-b640-8a0976c88346 | -6.679 | -42.8136 | 2025-10-02 13:30:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 112.2 |
| 618fe81e-dd84-3e79-9511-e600b4b500fb | -10.1462 | -50.2952 | 2025-10-02 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| fba34a8d-bbf9-3584-a0ce-db36871f9b42 | -14.7568 | -45.1985 | 2025-10-02 13:30:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 64d28624-554a-3c4a-9792-2fd2557d35c3 | -11.8234 | -45.0364 | 2025-10-02 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 048545f7-81c0-35c5-9801-76f935f6fca9 | -16.023 | -50.8553 | 2025-10-02 13:30:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 81c2ce6d-216c-38c6-98bd-35c0ac46a2e7 | -9.9031 | -45.978 | 2025-10-02 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 120d08dc-6f61-302e-a4ef-7c3567a2dc19 | -15.5379 | -45.2375 | 2025-10-02 13:30:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 141.2 |
| c0243132-3013-379a-be29-7a632ecd043c | -11.212 | -40.7359 | 2025-10-02 13:30:00 | GOES-19 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 95.4 |
| b5ea3d01-d399-3130-afd8-fa9848c4653d | -8.6722 | -47.6924 | 2025-10-02 13:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 444f3ec4-c25b-3a59-aaa2-35dec4bf416e | -8.5013 | -47.8404 | 2025-10-02 13:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 11b841d4-76df-3939-9499-108916071dec | -13.0119 | -45.1988 | 2025-10-02 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 118.6 |
| f8028205-80c3-3b3e-bb83-983abf2e1090 | -13.9585 | -48.1376 | 2025-10-02 13:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 60.4 |
| f1e8cd5b-c7fa-3b4c-af96-f475774eefdc | -10.1648 | -50.3147 | 2025-10-02 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 2abe6f1d-a426-35fd-b447-ace935e3a957 | -6.7163 | -44.6216 | 2025-10-02 13:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 1fdb77a6-a4ef-30ad-bde3-8c45087e8b6b | -7.8882 | -47.281 | 2025-10-02 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 5a5f20ab-2a76-3a62-bb59-9a3e98e6b3a9 | -7.7941 | -42.5369 | 2025-10-02 13:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 275.0 |
| 090ef9b2-8823-3a2a-b725-28653724e976 | -10.1648 | -50.3147 | 2025-10-02 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 46f1ff03-579b-3343-b7d0-a514c8fa0742 | -6.2138 | -44.2502 | 2025-10-02 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 8141c3f8-1dba-344f-b4a3-7537df453309 | -11.2803 | -47.8223 | 2025-10-02 13:40:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| a295b2c2-344e-32f4-89cb-33b6ea4adf81 | -9.8995 | -43.7003 | 2025-10-02 13:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 266.3 |
| f3548a3b-c582-351c-8b43-e6808ba85e33 | -9.9182 | -43.7212 | 2025-10-02 13:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 151.4 |
| 5c990e58-3592-3347-9f95-9c955dbbfe52 | -13.7859 | -48.0748 | 2025-10-02 13:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 31c8fbbb-e597-3b3e-908d-1e389be22275 | -7.7944 | -42.5132 | 2025-10-02 13:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 217.9 |
| 207c7cc5-5a65-3183-a9c1-a2ce96560c65 | -9.4272 | -47.5722 | 2025-10-02 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 97c3469c-2d6b-38ea-a719-b9588914b84b | -6.0997 | -42.4865 | 2025-10-02 13:40:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 95.8 |
| bd6fea54-b08a-3d1c-b8b3-9ccb832993dc | -8.8165 | -46.682 | 2025-10-02 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 150.3 |
| 7e4b9239-a97b-359e-8d71-69974b965ecb | -14.2121 | -46.1058 | 2025-10-02 13:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 142.1 |
| c3522299-4d8e-3232-b06c-fb8f754c0b1b | -6.2328 | -44.2257 | 2025-10-02 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| e667b7ab-4919-3955-9e96-620d84f38789 | -9.3392 | -45.7039 | 2025-10-02 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 183.9 |
| 7bb7e27f-27ef-3584-96f2-2a608432c3af | -9.8896 | -46.9226 | 2025-10-02 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| eeb2232a-571c-39c4-a751-72228b7fb4d2 | -12.7627 | -50.5567 | 2025-10-02 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 141.6 |
| e5e95f12-0e6c-3749-9801-6a2792669f2a | -15.5379 | -45.2375 | 2025-10-02 13:40:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 130.9 |
| bef97c43-c4ab-32d8-acdd-a542f1843d4f | -12.5001 | -50.2453 | 2025-10-02 13:40:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 4c764a09-e3e7-36be-9e41-12de69ae6ae8 | -9.9372 | -43.7187 | 2025-10-02 13:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 234.4 |
| ccc135e0-2282-3016-b23b-284c49315a3d | -14.425 | -46.1381 | 2025-10-02 13:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 164.8 |
| 2bfcb1de-3b78-3f93-ad77-449669cf0329 | -16.0421 | -50.874 | 2025-10-02 13:40:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 87.8 |
| f97863fe-97b4-34fd-9f08-ff129effa94d | -16.0225 | -50.8771 | 2025-10-02 13:40:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 68.1 |
| abaf3931-47b2-3aae-845e-5d1a01efc2c0 | -14.7043 | -49.616 | 2025-10-02 13:40:00 | GOES-19 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 441d5f0d-742f-3f00-8f6a-61549766bc41 | -14.4757 | -48.4137 | 2025-10-02 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 489cd858-e206-3c5d-b110-d3ff654eb6d8 | -11.1746 | -47.2805 | 2025-10-02 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| e49b02c4-cdde-355c-9208-df3e75fcfb8d | -10.937 | -46.6618 | 2025-10-02 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 133.3 |
| eb14578b-36ac-3cbc-940d-c88a35dc2e6a | -9.3199 | -45.7288 | 2025-10-02 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 4ce830b9-2fe8-3329-b18b-2e94a937e7ff | -8.5201 | -47.8386 | 2025-10-02 13:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| e5b4a06f-cd12-3084-a311-76809f4594ce | -9.3389 | -45.7266 | 2025-10-02 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 235.8 |
| af9823ee-facb-36c1-a1a6-44f13c1db96a | -8.7974 | -46.7063 | 2025-10-02 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| a0deeaf1-1e80-30a8-9e48-ea1f24f50a86 | -10.2025 | -50.3109 | 2025-10-02 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 2a6972fe-5477-34a3-b291-9547fbc053b0 | -9.336 | -45.9305 | 2025-10-02 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 244.6 |
| 48c72734-e6bd-3e84-8ccb-abf36bb73306 | -10.0337 | -50.2424 | 2025-10-02 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 80f49cc2-25a1-33df-a9e7-22e2444e251c | -16.023 | -50.8553 | 2025-10-02 13:40:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 110.9 |
| f7f1e566-9e2c-3418-a397-61edef83ff8e | -13.7876 | -51.1974 | 2025-10-02 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 1971a706-6520-36d3-9a20-6478033241b2 | -11.4796 | -44.9943 | 2025-10-02 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 325.8 |
| f9a0ba4d-0e38-328a-a7f9-16ecf1750503 | -6.679 | -42.8136 | 2025-10-02 13:40:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 117.2 |
| 868d368d-3404-38a8-9ed9-ff397ecd6e7c | -6.7816 | -45.5703 | 2025-10-02 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 7592b35e-9101-367f-990b-6207e9f38069 | -14.2924 | -45.977 | 2025-10-02 13:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 8708be31-0718-31ba-bc49-304656cf2b4b | -13.1743 | -47.8093 | 2025-10-02 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 2bd141ef-9b49-3520-8f29-1825d57326d0 | -6.7163 | -44.6216 | 2025-10-02 13:40:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| c7a93600-55f2-3e7b-9804-76cce6321c5d | -7.8879 | -47.3031 | 2025-10-02 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 181.5 |
| a122358e-4721-37ac-aa75-1b0a76192e5b | -18.1786 | -53.2809 | 2025-10-02 13:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 3a1694d7-9dd1-3714-825a-21961322e39d | -9.4086 | -47.5521 | 2025-10-02 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 142.1 |
| cbb77f45-2445-3e59-b4b0-204e4e7cd0b0 | -9.9376 | -43.6953 | 2025-10-02 13:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 43028296-91ea-3f3f-bca2-dcfc83ca996e | -8.672 | -47.7144 | 2025-10-02 13:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| f1f996a3-b79d-3a33-ba2a-3f9aff9d37cf | -11.8234 | -45.0364 | 2025-10-02 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 122.2 |
| b0c83769-cd3f-31a3-bf49-457b5e018a7a | -14.1917 | -46.1552 | 2025-10-02 13:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 1ae0fae0-51f7-384d-b171-8c308f3886ed | -15.2738 | -49.3073 | 2025-10-02 13:40:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 112.5 |
| ac4d639d-3ea4-3d66-aea3-cf15792cb371 | -13.7864 | -48.0524 | 2025-10-02 13:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 39f10b97-2735-3427-9648-ce3282c44481 | -18.1972 | -53.3423 | 2025-10-02 13:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 7e6490e6-eac2-31d2-a126-705c29695208 | -10.1459 | -50.3165 | 2025-10-02 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 2151e4c3-e54b-3310-be6e-fd85acbd1087 | -6.6976 | -42.8354 | 2025-10-02 13:40:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 106.0 |
| 95c762c0-3c09-3f71-8fa3-58953d7a98a3 | -8.2094 | -45.5301 | 2025-10-02 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 105.1 |
| c9cc0b2a-17bd-3793-a92d-f9765de3c5c8 | -14.4753 | -48.436 | 2025-10-02 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 97.0 |
| e6e0a74f-fcc9-3091-a605-71fe17c3e62c | -11.4792 | -45.0174 | 2025-10-02 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 82ae257e-24c1-3fc3-be87-db388f181565 | -10.0339 | -50.2211 | 2025-10-02 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 4122e6be-b282-343e-b593-1c269dd7bde5 | -6.7626 | -45.5944 | 2025-10-02 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| a77755f1-b878-394d-93e7-c0c745217ed2 | -7.1914 | -47.6257 | 2025-10-02 13:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| c55485ed-2a7b-3b8c-808b-1163c8942e83 | -9.9186 | -43.6978 | 2025-10-02 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 731c4c0c-30f7-353f-a9ec-542d74ae80fc | -6.2411 | -45.3198 | 2025-10-02 13:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 7cbb14a4-b7b3-3919-b220-31c653e1a2b2 | -8.6722 | -47.6924 | 2025-10-02 13:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 16b66252-ab5f-3827-ad5f-9c99bb962d2a | -7.7755 | -42.5152 | 2025-10-02 13:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 262.9 |
| db6023d8-b5f1-3cb2-8e6e-5223f0a6e64c | -11.8438 | -44.964 | 2025-10-02 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 60142660-9a30-3efd-9f23-639395a9e3cc | -8.1513 | -44.1397 | 2025-10-02 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 550b8fe0-75bb-34a4-9c96-92cbdc608619 | -14.3309 | -45.9933 | 2025-10-02 13:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 9a8c2c7a-fee8-3069-87cd-0f97a3ce7738 | -13.155 | -47.8121 | 2025-10-02 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 8b8c18fd-0bd6-34c0-b994-b6295184edf9 | -11.9276 | -47.8719 | 2025-10-02 13:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| b9ed7622-051a-30d1-8af6-5d836904d42c | -14.1921 | -46.1321 | 2025-10-02 13:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 03bdcfb4-a04f-3735-bf37-5aa812fba768 | -7.5661 | -42.656 | 2025-10-02 13:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 108.7 |
| 56dcfcfe-b32d-307a-835f-7f75335dbc3e | -8.6534 | -47.6943 | 2025-10-02 13:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 105.2 |


[Clique aqui para ver as próximas entradas](README156.md)

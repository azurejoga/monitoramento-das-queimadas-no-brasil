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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb91d722-a1cb-3ca1-8d5f-895806080f87 | -20.19251 | -46.20353 | 2026-09-27 04:12:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8335b29-51a4-328a-8253-f5aae35b0f4a | -22.17555 | -42.1224 | 2026-09-27 04:12:00 | NOAA-20 | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a531484e-fa0e-3b7e-b1f3-7c8570c1345e | -20.82292 | -44.9885 | 2026-09-27 04:12:00 | NOAA-20 | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 04e368c5-38a5-3631-8cf3-dc5bb65b26ef | -20.19326 | -46.1993 | 2026-09-27 04:12:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b9ba331-b43e-33d4-8b86-1aa8fa3258d1 | -22.76627 | -46.53372 | 2026-09-27 04:12:00 | NOAA-20 | PINHALZINHO | SÃO PAULO | Brasil | 3538204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6ae02746-b40a-3f2e-b594-714b2b0ee0e9 | -17.05179 | -56.58616 | 2026-09-27 04:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e50ce1ba-9102-3b67-a783-afbf5e5227ce | -23.56985 | -46.42522 | 2026-09-27 04:12:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f5e05914-462f-331f-b563-29c3fcaa4f54 | -17.04497 | -56.58443 | 2026-09-27 04:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 1f156fd7-c988-37e6-be07-8340f39db4a8 | -18.79735 | -48.04281 | 2026-09-27 04:12:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c9e2331a-620a-3108-b08f-26429640d5a3 | -21.52275 | -45.11234 | 2026-09-27 04:12:00 | NOAA-20 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a4586f56-bf47-3759-a0c8-5527458b7174 | -27.69368 | -49.14024 | 2026-09-27 04:14:00 | NOAA-20 | RANCHO QUEIMADO | SANTA CATARINA | Brasil | 4214300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 89d18754-f5d9-3cf4-9a14-bca054e08c0c | -8.33 | -44.2 | 2026-09-27 04:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0f83f025-d583-3eb3-b369-e7781607bded | -8.36 | -44.2 | 2026-09-27 04:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 44ea61b5-5a57-35f4-b325-1cb71de4fe77 | -8.36 | -44.16 | 2026-09-27 04:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b98e0855-44e4-31d7-90ca-111e3dc1fc83 | -8.33 | -44.15 | 2026-09-27 04:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 093836c7-9229-3904-8430-f1d53e613668 | -12.29 | -50.29 | 2026-09-27 04:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 67821300-d6e4-38c0-b2a7-b2e90e056024 | -31.86844 | -53.32975 | 2026-09-27 04:17:00 | NOAA-20 | HERVAL | RIO GRANDE DO SUL | Brasil | 4307104 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| f833a64c-2769-367b-8ec4-4087b050cc10 | -31.86421 | -53.32872 | 2026-09-27 04:17:00 | NOAA-20 | HERVAL | RIO GRANDE DO SUL | Brasil | 4307104 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 5f80c48e-06bf-3044-8ef3-ba685e577a21 | -12.2894 | -50.2927 | 2026-09-27 04:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 5ccd1b5d-09cc-3bae-86a5-730b9c1acf8e | -12.2703 | -50.2951 | 2026-09-27 04:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 5b9a6141-309b-3e42-bcb1-95204dad558a | -12.0369 | -50.6019 | 2026-09-27 04:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 23b9af51-3f3b-3ac5-95c1-2123438fa7d7 | -11.9431 | -50.5058 | 2026-09-27 04:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| f874f944-e186-381a-811f-d43b3fa53e8b | -12.0372 | -50.5804 | 2026-09-27 04:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| fa1a50da-0bde-3761-976f-95d706c58756 | -12.2897 | -50.2712 | 2026-09-27 04:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| d97937eb-cc0b-3213-bb47-30e7c0966747 | -1.24102 | -54.18814 | 2026-09-27 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba7662c4-1d54-37dc-b9c9-8cc64c8580db | 0.21173 | -51.32794 | 2026-09-27 04:49:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac70e762-baf8-35a4-ada0-335fa660c395 | 1.76943 | -50.82087 | 2026-09-27 04:49:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 137bf831-7698-3e2c-8a16-de819fdc8481 | -1.14969 | -54.09969 | 2026-09-27 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 641813ca-96f5-37b9-9267-75072b512431 | 0.49201 | -50.94389 | 2026-09-27 04:49:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a055f470-e247-3b0c-9534-577f1c070e30 | -1.03249 | -53.73163 | 2026-09-27 04:49:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a07dd4fd-28d5-3c3b-8335-df56de5eab5a | -1.33897 | -55.4772 | 2026-09-27 04:49:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d7184ae-c985-32cc-97e2-e572aa63b8ba | -1.15091 | -54.09199 | 2026-09-27 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2265a894-70f3-3be0-9f26-e9d06a7cb086 | 0.46821 | -50.98617 | 2026-09-27 04:49:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b32a62ab-a3bf-304b-82b0-505717cdf3d3 | -1.85931 | -47.97786 | 2026-09-27 04:49:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28aec349-b000-34dd-b885-84bfc00699c7 | 1.13522 | -50.72725 | 2026-09-27 04:49:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96e6a3d2-f436-3dc7-b414-989ded9be5c8 | -1.14046 | -54.09036 | 2026-09-27 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c47a8151-05cd-3a16-9f40-901f3ce794e9 | 0.6977 | -51.43452 | 2026-09-27 04:49:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ad0df454-7bcb-3293-9a74-d9398bacc675 | -0.51772 | -49.13163 | 2026-09-27 04:49:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a6e5625c-ed3b-3a23-919b-d718f5d623da | 1.65622 | -55.93711 | 2026-09-27 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce76d341-6472-3c0e-9077-48798e6a50b3 | -1.21804 | -54.56234 | 2026-09-27 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5692c4fc-b852-30e2-8446-c40457220e1c | 1.96533 | -50.90279 | 2026-09-27 04:49:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d20e12b6-a913-3a3b-a6ea-e0c698529775 | -2.09619 | -48.95398 | 2026-09-27 04:49:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1afa5f1b-8726-39b6-a37c-c362c9d16bd3 | -1.03307 | -53.72796 | 2026-09-27 04:49:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3a0e6fe-cf8e-3114-a294-8e1f2b8a3ee4 | 1.1405 | -51.17189 | 2026-09-27 04:49:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d948cea5-6006-3dc4-ae42-65bd02c77cd7 | 0.25875 | -50.93138 | 2026-09-27 04:49:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0240f7ee-f26f-332b-af8d-4da9a95105d1 | 2.94079 | -60.31937 | 2026-09-27 04:49:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abef85de-fb8f-30c1-b2ec-d6ab4dbeb5d0 | 1.66135 | -55.95771 | 2026-09-27 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a1bed202-6ff8-30d1-86e6-78d8e12658a9 | 0.32908 | -51.44657 | 2026-09-27 04:49:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02b35407-6e23-34c2-bc46-0d6294ee6eb8 | -2.00092 | -47.01114 | 2026-09-27 04:49:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54550ed5-928c-3d21-97d7-67a4afee0e34 | 2.63563 | -60.17332 | 2026-09-27 04:49:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81679137-5898-3815-9aa5-ec2a1c76f22b | 1.33447 | -50.99761 | 2026-09-27 04:49:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75a57cf6-00d2-3b25-9ef3-eab13a0e5daa | -1.22985 | -54.12336 | 2026-09-27 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4536cdd9-7cc6-3bee-ac8f-8a7c19fa18fb | -1.21929 | -54.55439 | 2026-09-27 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2f2881b-b6f9-3f0d-840a-85ecaf0923ee | -1.22469 | -54.12257 | 2026-09-27 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8a73e3c4-d07e-38cd-a3b8-ee1bc00ebf2c | 1.06405 | -51.12063 | 2026-09-27 04:49:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e466ac5-b44b-3f9d-a558-7154d25021c1 | 1.64658 | -55.92791 | 2026-09-27 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c44c092-fc8a-38c7-b521-5ba112db749d | 1.66352 | -55.95745 | 2026-09-27 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3dbe4bc4-067d-3548-9cb1-5b6d784d7607 | -0.50672 | -49.13384 | 2026-09-27 04:49:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9bd58740-cd6d-381c-b8b2-0b47d8f10622 | 0.20843 | -51.32845 | 2026-09-27 04:49:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f176f5cc-a422-323b-a6e0-fb00068d9589 | -1.14333 | -54.09477 | 2026-09-27 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d95a8cb-e209-3046-8305-d6433a066f45 | -1.22817 | -54.12316 | 2026-09-27 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8a15fe7-8e84-33f2-92f0-277a19c51f00 | 0.47988 | -50.95278 | 2026-09-27 04:49:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0c208fdb-ced3-3d67-b411-7781ba8314ca | -1.14107 | -54.0865 | 2026-09-27 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7dd3abab-bf73-3b9d-acfd-4db1d22ccb1a | 1.65113 | -55.93076 | 2026-09-27 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36f4de03-0d2e-3a70-a0fe-b5236790f6b1 | 2.63734 | -60.17279 | 2026-09-27 04:49:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27c69128-cf3e-3f9f-9e22-f141052a931c | -1.2178 | -54.22126 | 2026-09-27 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 08a88cca-0f9b-3c7d-b1f1-8f46bb051f14 | -0.5189 | -49.12399 | 2026-09-27 04:49:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f372ef03-b9cf-3a60-b6a9-32fab290bcea | -1.14455 | -54.08705 | 2026-09-27 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ad43aa5-ca95-36f0-a91b-85d32040e6fb | -1.14394 | -54.0909 | 2026-09-27 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0410a158-d870-3ca0-9e62-ccfb64647ce0 | -1.21342 | -54.54538 | 2026-09-27 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd2860e6-7f1b-3a08-8d4f-77cdab5d7440 | 1.96587 | -50.90622 | 2026-09-27 04:49:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 81499e96-e483-33ec-9db9-fd9444a7d69f | -0.50325 | -49.1333 | 2026-09-27 04:49:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d3cf299-684b-3828-84b0-cf657ff2d92f | 2.89476 | -60.27457 | 2026-09-27 04:49:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8596b3fa-0b9a-3552-9cbe-23c63282a108 | 0.701 | -51.43401 | 2026-09-27 04:49:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4e559591-9094-3cfa-899d-068ed002b7ba | -2.36493 | -48.52311 | 2026-09-27 04:49:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d58d987-1b84-3fed-b3c3-09f266436f04 | -0.18763 | -50.34119 | 2026-09-27 04:49:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98236481-6dbc-3cad-a790-20a452e5b464 | -1.04429 | -53.56659 | 2026-09-27 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3a2d66d5-5141-340c-8de9-feda9f2d2151 | 1.66187 | -55.96121 | 2026-09-27 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2acfd383-bb7c-3dbb-b903-f24f52b03ee6 | 1.65276 | -55.94119 | 2026-09-27 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a2f448b6-fa25-3058-a85e-b59192f9dc02 | -1.41152 | -54.62251 | 2026-09-27 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| abb76e9d-ffd7-32ea-b6e8-4142fc055674 | -0.51484 | -49.12728 | 2026-09-27 04:49:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bef1ba33-5708-38c8-90f6-e7e298cea593 | -1.86304 | -47.97845 | 2026-09-27 04:49:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 86e416ba-0d1e-3e3e-8c1f-0eb3d88d04bc | 1.96257 | -50.90673 | 2026-09-27 04:49:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a9414747-1bc7-38eb-8ff6-02ccfcad8ae9 | -1.04886 | -53.55977 | 2026-09-27 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7b7c96e4-3278-3aaa-8744-53da890129e4 | 1.1438 | -51.17139 | 2026-09-27 04:49:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c6d93c81-d0d2-32ef-bac2-d883c9059563 | 0.48871 | -50.9444 | 2026-09-27 04:49:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9ee91c6d-477d-33ca-a8b9-d4cd1172b918 | 1.64496 | -55.91754 | 2026-09-27 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a04a0461-34e7-3587-9887-0e0e59db7473 | -1.22131 | -54.22178 | 2026-09-27 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b9dc6fc-26a5-372a-9198-868a846f43d1 | -1.21866 | -54.55837 | 2026-09-27 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb90a0cf-90b4-3925-b16b-eba63ae25809 | -1.30374 | -54.22219 | 2026-09-27 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06de8cf5-2286-34bd-b711-3012a24b4ccd | -0.52178 | -49.12835 | 2026-09-27 04:49:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8fa3ddd-8c11-38da-91ae-f764e910267b | 2.94134 | -60.32304 | 2026-09-27 04:49:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd62882c-616f-3870-b31a-d17de7c01243 | -0.32979 | -48.51875 | 2026-09-27 04:49:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5933566e-0b71-37fd-939b-f1b488d47a9d | -0.50731 | -49.13002 | 2026-09-27 04:49:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 80cab7df-dd03-30a1-8f38-74626849c66e | 1.65222 | -55.93771 | 2026-09-27 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a160c9ff-c81e-3ece-b2b7-15a0a8e74dda | -0.51543 | -49.12346 | 2026-09-27 04:49:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6f0de5f4-166a-3160-829b-e25965ef325d | 1.6624 | -55.96469 | 2026-09-27 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e53eda9-e64a-3c9b-929c-3e88c4589687 | -0.54063 | -49.1898 | 2026-09-27 04:49:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b8d06d1a-f6ed-3d7b-ae9f-34ad37dfa959 | 1.13799 | -50.72331 | 2026-09-27 04:49:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29161733-069e-300f-8fb5-465dc652d25f | -1.04486 | -53.56291 | 2026-09-27 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README23.md)

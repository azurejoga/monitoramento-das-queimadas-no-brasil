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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b73dac4f-aeba-3c55-a73e-e5f7b5b55f10 | -12.3709 | -52.4701 | 2025-01-07 00:00:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 7291c37f-f6fe-30a8-ac41-e20a98b6d2f0 | -9.8725 | -36.2972 | 2025-01-07 00:00:00 | GOES-16 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 145.0 |
| da00049e-d36e-3cff-b219-902e91902590 | -9.8532 | -36.3006 | 2025-01-07 00:00:00 | GOES-16 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 101.5 |
| ec9b8552-2b8e-3141-860d-8c1811b8cdb2 | -9.873 | -36.2702 | 2025-01-07 00:00:00 | GOES-16 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 180.4 |
| cc93d844-471b-3588-9bc1-ce8b4546011d | -12.3515 | -52.4932 | 2025-01-07 00:00:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 8a1326b5-ebd5-3d5d-9efa-3c910d95ffd3 | -12.3706 | -52.4911 | 2025-01-07 00:00:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 667fad25-ed35-3771-bacd-97a9c08519a8 | -9.8537 | -36.2736 | 2025-01-07 00:00:00 | GOES-16 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 119.1 |
| 8789e3ad-367c-31bb-850b-0f04bb0d6e66 | -12.3515 | -52.4932 | 2025-01-07 00:20:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 7c4ec5fa-5053-3b68-8376-6576db860fd9 | -12.3706 | -52.4911 | 2025-01-07 00:20:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 101.4 |
| ef96b675-6f8b-3a05-9336-b2ac352bbc21 | -12.3709 | -52.4701 | 2025-01-07 00:20:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 6da5de6b-c359-3795-bf6b-ff6c6471ecfe | -22.55388 | -47.31692 | 2025-01-07 00:28:00 | TERRA_M-M | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ba7a6d13-a5cb-33f0-9775-73cddd8aef87 | -12.83812 | -39.79816 | 2025-01-07 00:30:00 | TERRA_M-M | ITATIM | BAHIA | Brasil | 2916856 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 0ee9209c-cd2a-32c1-bc7c-0b873dc5d570 | -12.71566 | -40.21513 | 2025-01-07 00:30:00 | TERRA_M-M | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 645a23d0-ed4a-3d11-9b2f-8fe6241d36b9 | -13.75654 | -39.9677 | 2025-01-07 00:30:00 | TERRA_M-M | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| eed7a8b7-d1f1-37bd-a76e-3862ef29b526 | -12.83365 | -39.42212 | 2025-01-07 00:30:00 | TERRA_M-M | CASTRO ALVES | BAHIA | Brasil | 2907301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| b7c80efa-50fa-3394-8fce-773cdd24e6d3 | -10.09635 | -36.23591 | 2025-01-07 00:32:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 91.0 |
| 39aad182-c7ac-332b-a4cf-af91c1ee1c67 | -10.09947 | -36.24112 | 2025-01-07 00:32:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 74.1 |
| db004eec-cad7-3904-8b42-44f888f96ca1 | -9.46915 | -36.15059 | 2025-01-07 00:32:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 33.4 |
| 550476d1-baab-30bf-901f-1d61845f7c5c | -8.54241 | -35.74434 | 2025-01-07 00:32:00 | TERRA_M-M | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 27.8 |
| 62954c4c-b5b5-3030-848f-18fac0c850b5 | -10.09612 | -36.22004 | 2025-01-07 00:32:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 31.9 |
| 1e1fcb6e-9199-3b38-b2b3-d5c332d060fc | -10.08045 | -36.37235 | 2025-01-07 00:32:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 1d852168-2e1b-3a65-b325-9936ab699dcc | -8.53779 | -35.75012 | 2025-01-07 00:32:00 | TERRA_M-M | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 32.0 |
| c6f51377-3bbc-3bc6-a7dd-7ec9ae641491 | -9.91631 | -36.01398 | 2025-01-07 00:32:00 | TERRA_M-M | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| cc5d4af2-ac73-314b-8f1a-b71d6be98c45 | -9.86777 | -37.10496 | 2025-01-07 00:32:00 | TERRA_M-M | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 4db98ec3-0da6-3ff8-82fb-2e1a4569abfe | -9.47773 | -36.14247 | 2025-01-07 00:32:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| 172d5e1a-070f-35df-938b-54eba029db2c | -10.87394 | -40.42679 | 2025-01-07 00:32:00 | TERRA_M-M | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 82516f9a-46e3-3924-9822-8db63736b3fd | -9.1176 | -35.33859 | 2025-01-07 00:32:00 | TERRA_M-M | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 22.2 |
| edc87659-a28c-3ba0-8d96-6e631279a3be | -9.78878 | -41.76874 | 2025-01-07 00:32:00 | TERRA_M-M | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 45094da9-6cb1-3e38-813e-618a057de277 | -12.3709 | -52.4701 | 2025-01-07 00:40:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| bebdc65a-9c50-38ff-b268-164342d9d080 | -10.1974 | -36.4278 | 2025-01-07 00:40:00 | GOES-16 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 115.8 |
| db708397-772e-3cd6-b419-d32c1bbec56d | -12.3515 | -52.4932 | 2025-01-07 00:40:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| edee65a8-c878-3093-a8f6-6fb4c546335f | -10.0829 | -36.3676 | 2025-01-07 00:40:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 108.8 |
| 45101a30-2634-39f4-90ac-d04157fe08e6 | -12.3706 | -52.4911 | 2025-01-07 00:40:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 5f4a0369-d9f5-3d16-85e9-ecd4178a1186 | -12.3515 | -52.4932 | 2025-01-07 00:50:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 2aed11cb-5911-3f36-9003-914f40b599b1 | -12.3706 | -52.4911 | 2025-01-07 00:50:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 28f0b41b-d3a1-3ecb-a498-06e06a6534a0 | -12.3515 | -52.4932 | 2025-01-07 01:00:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 33c4a58c-14e7-3022-8e91-fef3ace40f38 | -12.3706 | -52.4911 | 2025-01-07 01:00:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 53680c82-d5c1-3c2c-ba2b-0fc466556655 | -12.3706 | -52.4911 | 2025-01-07 01:40:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| ee1a87e6-8c55-3699-a626-4cea6af1e821 | -12.3706 | -52.4911 | 2025-01-07 01:50:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| bb303d16-1204-3d9f-ad66-063e15c938bb | -12.3706 | -52.4911 | 2025-01-07 02:00:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| cad14051-77bc-34ba-b7c0-fbee505e619c | -5.87636 | -35.38279 | 2025-01-07 03:10:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e36019f5-84aa-31c3-b98f-98fd47b1409f | -5.88134 | -35.38366 | 2025-01-07 03:10:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5ca66283-35fe-3c88-803b-ef69756d8fec | -6.86294 | -35.15423 | 2025-01-07 03:10:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 39387f5d-7740-349e-8d4a-9892ae1dea3e | -6.8581 | -35.1535 | 2025-01-07 03:10:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b55cac83-3e45-3220-be28-64fa7fb8265e | -5.88085 | -35.38428 | 2025-01-07 03:10:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 6.8 |
| bc9cbec0-b1eb-31e4-a0a4-7a30064b223c | -10.3195 | -36.72175 | 2025-01-07 03:12:00 | NPP-375D | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 85ec5586-939e-3bb0-9ed3-45ff3b2a54ed | -10.53622 | -36.88718 | 2025-01-07 03:12:00 | NPP-375D | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 512dd3d2-0939-31c5-9f06-5bc1b1ba5a0d | -10.54126 | -36.88836 | 2025-01-07 03:12:00 | NPP-375D | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f7473df0-e07c-3b65-983f-faaa2e714642 | -10.18583 | -36.27538 | 2025-01-07 03:12:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4bfb7d17-62e2-3639-8a35-8dcfdb52503b | -7.78949 | -37.39359 | 2025-01-07 03:12:00 | NPP-375D | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ab1f0351-401e-32e6-9389-387379007a18 | -7.82827 | -35.23216 | 2025-01-07 03:12:00 | NPP-375D | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| c9bef669-7f2a-37a5-916a-4b9f11252f9e | -10.17992 | -36.27997 | 2025-01-07 03:12:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f68a0f51-36af-3cba-a79d-6190ed9c7074 | -8.53561 | -35.74971 | 2025-01-07 03:12:00 | NPP-375D | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 075439ed-37c3-3671-87f9-9b9f4962f7d9 | -10.06169 | -36.33525 | 2025-01-07 03:12:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0b8b01e5-f805-33ff-85d3-e33ba2edc809 | -7.67971 | -35.27059 | 2025-01-07 03:12:00 | NPP-375D | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cdadf888-3a32-3989-a760-9aea5ee9ea13 | -10.2169 | -36.38635 | 2025-01-07 03:12:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| bb5719c5-4642-3b2d-9bd6-cf341b9e7261 | -10.22177 | -36.38641 | 2025-01-07 03:12:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 28437200-2d5d-352e-8747-4314897efa4d | -10.21781 | -36.37997 | 2025-01-07 03:12:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d1aa9d0b-5a29-352c-9b98-f23afa22aa57 | -10.32006 | -36.71873 | 2025-01-07 03:12:00 | NPP-375D | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 16cee6dd-5ee6-34d9-b543-82c984002a8f | -10.21681 | -36.38552 | 2025-01-07 03:12:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4ebf29ce-ef45-32bd-b7b9-11dc46d9bbe3 | -10.54182 | -36.88529 | 2025-01-07 03:12:00 | NPP-375D | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7b6ba997-d981-3785-83fb-6b7eba854ce7 | -10.18093 | -36.27443 | 2025-01-07 03:12:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5378039e-66b7-35de-8b4b-bb19cf4801b3 | -8.53672 | -35.74352 | 2025-01-07 03:12:00 | NPP-375D | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 397b949c-6383-3a55-ae06-f35150eaf9d0 | -10.22287 | -36.38176 | 2025-01-07 03:12:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 348d61fe-2544-336d-b4fc-82e01c926c2e | -10.18482 | -36.28093 | 2025-01-07 03:12:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2987908a-cfd0-311e-a87a-10307e7de043 | -7.82929 | -35.22963 | 2025-01-07 03:12:00 | NPP-375D | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| d2dae7fc-3ca4-31a2-823a-aef81c177c2f | -8.42562 | -35.23975 | 2025-01-07 03:12:00 | NPP-375D | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 646367f7-7c32-3318-a89f-c4c8704e88a8 | -7.68062 | -35.26541 | 2025-01-07 03:12:00 | NPP-375D | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 48596ee8-936d-3d64-83b7-675c1b492b53 | -10.53677 | -36.88417 | 2025-01-07 03:12:00 | NPP-375D | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 1a1ed716-d788-3ef5-a5f1-f604bdd3a236 | -10.22275 | -36.38093 | 2025-01-07 03:12:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 9bb1cb86-35b9-308e-8f32-8771b70dd3ab | -9.01484 | -35.40195 | 2025-01-07 03:12:00 | NPP-375D | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2bd0c62b-6f76-3e63-b541-32612688c828 | -7.8245 | -35.22889 | 2025-01-07 03:12:00 | NPP-375D | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 59f63b3e-a262-364f-8cdf-fe962333d822 | -10.53564 | -36.89032 | 2025-01-07 03:12:00 | NPP-375D | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8457bd7e-61e6-38e5-9886-dc08186829ff | -10.21794 | -36.3808 | 2025-01-07 03:12:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 3a5a0a49-1fe2-3712-928b-b7d86f0997c4 | -12.83184 | -39.79768 | 2025-01-07 03:14:00 | NPP-375D | ITATIM | BAHIA | Brasil | 2916856 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9db6fd11-a0b2-3d2d-9c8b-654190800db3 | -12.83767 | -39.79913 | 2025-01-07 03:14:00 | NPP-375D | ITATIM | BAHIA | Brasil | 2916856 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 84498f50-c6e9-305a-8ad5-65378cc6b2a3 | -12.83677 | -39.80362 | 2025-01-07 03:14:00 | NPP-375D | ITATIM | BAHIA | Brasil | 2916856 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6d0043bf-c028-361a-897a-c6ef197935ed | -2.9382 | -40.1833 | 2025-01-07 03:32:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 1eaf529c-b6e5-3426-abf4-a22733c0327e | -9.55818 | -38.29166 | 2025-01-07 03:34:00 | NOAA-20 | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dd5852ee-dfc6-3f11-8c24-6599e0e97db0 | -8.53413 | -35.74743 | 2025-01-07 03:34:00 | NOAA-20 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| 384ceb49-e579-3440-937b-fbd31931863f | -10.53963 | -36.88886 | 2025-01-07 03:34:00 | NOAA-20 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a2adc3bd-593d-3c8d-a3d3-418a45bc6823 | -10.08072 | -36.15711 | 2025-01-07 03:34:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 18ca2594-c7a4-3b45-8f47-5f5019ff8ec6 | -3.72713 | -39.96109 | 2025-01-07 03:34:00 | NOAA-20 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4038585f-d5c1-38df-aaf2-ee2924b7832a | -9.56196 | -38.29225 | 2025-01-07 03:34:00 | NOAA-20 | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fe9ed1de-133a-3951-b542-e9d1706c2bf1 | -7.5701 | -35.19918 | 2025-01-07 03:34:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fbecb454-0553-3bb1-a4df-1a1db3637c21 | -10.06257 | -36.3334 | 2025-01-07 03:34:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7bcc13a8-5dd5-35f1-a96d-02e13147f179 | -8.37464 | -35.7555 | 2025-01-07 03:34:00 | NOAA-20 | CAMOCIM DE SÃO FÉLIX | PERNAMBUCO | Brasil | 2603504 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 593f4ce6-af16-3b7b-910f-14eefe060cb6 | -10.53615 | -36.88824 | 2025-01-07 03:34:00 | NOAA-20 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 24.9 |
| 007fd03e-da80-36ad-b704-5e5f22ac40f4 | -7.68142 | -35.26855 | 2025-01-07 03:34:00 | NOAA-20 | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0b5b8604-3783-32b1-82c7-b60cad9a8d0f | -9.78593 | -41.77013 | 2025-01-07 03:34:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d913af57-1a8b-3c84-b40f-cdc96704d560 | -10.22313 | -36.38257 | 2025-01-07 03:34:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 63c16ce8-2492-30c3-83f8-35465184226a | -8.53534 | -35.73999 | 2025-01-07 03:34:00 | NOAA-20 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9ccc5728-e1a6-3f46-81a2-feeef33d8680 | -8.53874 | -35.74049 | 2025-01-07 03:34:00 | NOAA-20 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a6a5674c-6505-36b5-9506-48e0137204ea | -7.82368 | -35.23194 | 2025-01-07 03:34:00 | NOAA-20 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 531f55ad-917f-337d-8d3b-b6e49d19c578 | -8.06516 | -35.12397 | 2025-01-07 03:34:00 | NOAA-20 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b6e31dba-fdcc-3b45-9bd7-2b29d78720ae | -8.53474 | -35.74369 | 2025-01-07 03:34:00 | NOAA-20 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| 9ac2a2fa-bbee-3a0f-922f-fd4d55b49df9 | -8.53814 | -35.74417 | 2025-01-07 03:34:00 | NOAA-20 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 22110e6c-ee48-3856-9c7a-279ce32d4429 | -10.08112 | -36.15671 | 2025-01-07 03:34:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 12caf1d4-d0a0-37dd-9420-ac198f5d0bd9 | -7.78945 | -37.39563 | 2025-01-07 03:34:00 | NOAA-20 | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9a50c9a5-efef-3650-8335-2a4ccd63cf9f | -8.24832 | -35.2739 | 2025-01-07 03:34:00 | NOAA-20 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |


[Clique aqui para ver as próximas entradas](README2.md)

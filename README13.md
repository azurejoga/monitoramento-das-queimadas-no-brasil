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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7902bc7-2237-30a5-b6a6-349e0f3fbcda | -11.43367 | -55.00277 | 2025-06-03 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdf87253-a3b1-391c-a8f0-3b0522dd73fc | -12.4574 | -54.91348 | 2025-06-03 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 307b4b9a-d18f-3a99-bdf7-86f1598d3bef | -10.50029 | -53.64686 | 2025-06-03 05:12:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 683782f3-888b-30db-8926-cdd0ea343f75 | -13.72087 | -58.67221 | 2025-06-03 05:12:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77190d21-b251-3b84-8862-4aeb60896310 | -12.09066 | -54.57409 | 2025-06-03 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1326e638-d529-3037-b2e1-6572a48101e8 | -10.24051 | -52.22598 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0e3c2153-ef07-37ea-a060-87044a39f2ac | -12.37492 | -54.16534 | 2025-06-03 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59b0d01e-3c07-3945-93ff-aabb27fedf66 | -11.79342 | -47.38489 | 2025-06-03 05:12:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dadb8ec6-91c3-3a2b-ac28-0c881290b0a2 | -11.43735 | -55.00335 | 2025-06-03 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95d484e8-398d-358f-9364-3bbd0353bf0b | -12.10093 | -54.66702 | 2025-06-03 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0d8f79a-5b90-3a18-b714-105104be8729 | -9.23877 | -63.29294 | 2025-06-03 05:12:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a0e7fd8e-151a-33ae-821d-1171bddd5efb | -11.90005 | -56.40932 | 2025-06-03 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c61a953-4939-377d-9261-7c12cd3e92b6 | -11.55347 | -56.42912 | 2025-06-03 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| acbc6a9a-0f52-3a2e-9cf4-8695465fc91e | -9.43325 | -62.46404 | 2025-06-03 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fdfdc4b-861d-3a03-9e14-119afab49c52 | -12.66519 | -58.21973 | 2025-06-03 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e15740ef-a38e-37e5-8828-8c0d7ee7d6fa | -10.45593 | -47.9398 | 2025-06-03 05:12:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7e47f7e8-4df0-3375-a6ae-d621364a1a21 | -9.87496 | -49.34127 | 2025-06-03 05:12:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 60bfcea2-5e08-303f-a02d-03eaeacc6016 | -10.46744 | -47.94163 | 2025-06-03 05:12:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52dee085-949b-353f-8a1b-2502fb2a6939 | -11.92455 | -54.81557 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52055202-c999-39fc-928e-e5ed5c2ff5b1 | -9.6058 | -49.02263 | 2025-06-03 05:12:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e93d1b82-45fd-3319-a7f5-1a3dcf4e3f0f | -11.43431 | -54.99835 | 2025-06-03 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 198bf254-6b2d-3330-bf76-5229f718403c | -9.7224 | -48.31821 | 2025-06-03 05:12:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1d9d851-204f-31b5-8ee7-e36393de4ffc | -10.14173 | -52.14268 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 417f6744-187a-3997-92b4-71299a8d8acc | -11.64723 | -55.36572 | 2025-06-03 05:12:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15c37d86-b271-3d80-8b5b-e563623f4d47 | -9.61154 | -49.02002 | 2025-06-03 05:12:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6ddc5919-86d0-3919-ab81-43de6975ee1b | -10.2388 | -52.21947 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b8359ee-9f9b-3ca3-baf6-4df5e342838e | -13.72418 | -58.67274 | 2025-06-03 05:12:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ad4e284-4195-37e3-9c02-8ce226c031d7 | -9.33384 | -63.52065 | 2025-06-03 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 372be89d-f6ec-3b21-82b3-8add9a264f2b | -12.09715 | -54.66645 | 2025-06-03 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efaf6809-2353-3001-9faa-67b543035f27 | -11.55404 | -56.42529 | 2025-06-03 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 82accfb1-ab78-3e73-a2e2-376a025e0ddc | -14.02616 | -55.13474 | 2025-06-03 05:12:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f447e075-c54e-3f23-8b2a-b8dcf2e9e0b2 | -11.90578 | -47.44778 | 2025-06-03 05:12:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4702be98-c711-3e5a-b628-1f941fb067b6 | -12.67236 | -58.21725 | 2025-06-03 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47a5745a-943b-3117-8756-9ecf1ba648b1 | -12.08557 | -54.58292 | 2025-06-03 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d9c8e5cb-5545-3b4e-ab01-bbe098cd2600 | -11.25697 | -49.49939 | 2025-06-03 05:12:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aea2f1ce-f314-312f-925e-55ed1e5902d0 | -12.36641 | -54.1693 | 2025-06-03 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8979e6d5-4d7d-3b53-b140-3044650dd63c | -11.43304 | -55.00718 | 2025-06-03 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1221ff73-e1d5-32fb-9725-d92e3a610ac4 | -10.82372 | -56.94504 | 2025-06-03 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 366e7f31-0d7f-312b-b0fd-e77188c1ad68 | -12.12359 | -54.67042 | 2025-06-03 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b8922cc-e2ce-35c3-9467-ce9dfb3e92fc | -10.14232 | -52.13852 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 47f63a59-55fb-3902-91f0-cb935ed8c701 | -11.40725 | -52.9463 | 2025-06-03 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2a432e6-06b7-3dd3-88c6-e88bfe71fb99 | -10.14003 | -52.13729 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c46d7b63-6d81-3de1-8eaa-db1bf6b9bf25 | -12.08177 | -54.58236 | 2025-06-03 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed305e14-ab6b-3b4e-9db6-7782043267c4 | -10.23996 | -52.23017 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 046417f1-f69a-3376-930b-6538d8993954 | -10.01416 | -67.00616 | 2025-06-03 05:12:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9034f04-5b0d-3c1f-b875-b746d905a13b | -12.45936 | -54.91658 | 2025-06-03 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f56eac8f-19d2-3df4-aa55-71a0e28b737c | -11.43671 | -55.00776 | 2025-06-03 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8de96a4e-07f2-37f6-82f1-ace0e528f9ae | -14.03435 | -55.13114 | 2025-06-03 05:12:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9054aa8c-918b-3b20-b85b-6b9b95b817da | -10.14435 | -52.13795 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b1f1a6b4-e124-3004-959a-f13633777672 | -14.01797 | -55.13831 | 2025-06-03 05:12:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 953d15ba-f414-3b35-990d-f4f6e9b07c92 | -12.17335 | -54.26019 | 2025-06-03 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2db0475-6425-3a35-9ae1-e6524acf4e02 | -10.46797 | -47.94318 | 2025-06-03 05:12:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 36cce145-03a3-36be-8352-9bf0ad4b2b7d | -11.91951 | -54.82409 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| fc27a151-d3b0-3136-8a84-f68b2b3234ba | -9.23938 | -63.28933 | 2025-06-03 05:12:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9352174d-e9fb-3634-b79e-2e5ccaefd960 | -11.58139 | -47.44872 | 2025-06-03 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 73367e0a-5dce-3081-bbf5-d263f7dd56c6 | -12.52221 | -57.17016 | 2025-06-03 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42f6bfaa-02fd-3217-9e57-d0c11d5c0636 | -11.91643 | -54.819 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| edc7df33-c2c8-32b0-8522-04c60d0b2f2a | -12.33752 | -54.98388 | 2025-06-03 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20762d20-d7b8-3fd4-b740-3dce9673ced6 | -10.24193 | -52.22844 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bc6779c8-f0f1-3750-b6c5-d0e852f5fa5b | -10.138 | -52.13788 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dc2e928b-dfaa-373e-9897-a09de1878f90 | -10.23621 | -52.22535 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e5ebbf6-bd81-3646-ae4b-6a752cc01013 | -12.08229 | -54.57991 | 2025-06-03 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6df742db-6248-3c0c-b5fb-08162edbe329 | -14.02682 | -55.13002 | 2025-06-03 05:12:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76e6518a-28a7-38e0-a1fc-e6a1d3dddd7b | -11.56036 | -56.43016 | 2025-06-03 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 090d9796-5d9e-31c7-af72-e2d8f5144f5d | -12.19661 | -54.26353 | 2025-06-03 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea41fb19-8e1f-3131-b3bc-cef00ebaf3f3 | -13.48192 | -56.55828 | 2025-06-03 05:12:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d15c45f9-70f3-3d77-b03a-f478e3492c79 | -12.46114 | -54.91404 | 2025-06-03 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68434d1e-ef89-31cb-9a79-0d69dc772e6a | -10.24252 | -52.22426 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e6f6a45-fd1f-3c42-aaaa-96346ffb3c3b | -14.02061 | -55.11938 | 2025-06-03 05:12:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2663ae29-dc4b-3edb-8fe9-e4b562ae375d | -11.58192 | -47.44407 | 2025-06-03 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 55311e57-7c9a-32ec-a1ea-589052752e91 | -10.46117 | -47.94482 | 2025-06-03 05:12:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6aa90fb-bc8b-3928-a178-4bda37d23933 | -9.40995 | -62.4476 | 2025-06-03 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11b9f8a5-740f-3ca2-9085-f7648e95f577 | -11.9098 | -54.78538 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5ff62c94-63dd-3a1f-bdf0-f60b0517db53 | -10.69546 | -57.6506 | 2025-06-03 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6763b752-d160-3b3d-9616-a2081f3eefc6 | -11.83467 | -58.81326 | 2025-06-03 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 18f5e25a-b9e8-3986-ae51-57f8093e2edd | -11.90101 | -54.79343 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 9494ef97-1c66-34b5-98c2-5fc8efe43117 | -10.46692 | -47.94574 | 2025-06-03 05:12:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1715c106-1a00-395a-8084-cd84ebbbaeb3 | -14.03369 | -55.13587 | 2025-06-03 05:12:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6315390-f44e-3bd1-b446-efa583b27471 | -12.36572 | -54.17434 | 2025-06-03 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef185b3d-a586-3ad4-ad13-a9441ad68b47 | -9.96439 | -64.96143 | 2025-06-03 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17177cfe-bfc2-3cc5-8dd2-cbd18dba64ab | -11.9054 | -54.78942 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| e26564e7-6cbb-368b-b025-fc302983feeb | -11.90166 | -54.78887 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 22615ca4-f126-3028-b9ec-645a68841c4e | -11.57926 | -47.45235 | 2025-06-03 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5d3a19fb-3b57-3bea-9b9f-9967e8f13762 | -11.90629 | -47.44314 | 2025-06-03 05:12:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 31aed4fb-38f6-30fc-b620-bb9e05ebce85 | -12.67181 | -58.22078 | 2025-06-03 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd7574e3-11da-3b9e-9da1-38d255993964 | -11.25737 | -49.49611 | 2025-06-03 05:12:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7dfa110-a4f2-3f59-ad58-582b211deb3d | -12.16879 | -54.26454 | 2025-06-03 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d83a158-13f5-38fd-9d13-d61cd6a4b1f5 | -10.23391 | -52.223 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 90e0edb0-3ec9-3224-924d-c3c3f812e542 | -11.65507 | -55.36256 | 2025-06-03 05:12:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8e61b51-d585-3bf7-890a-bf755f2daaf2 | -12.10028 | -54.67168 | 2025-06-03 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c77df4fb-8eb3-3e46-8714-383c5b293e29 | -11.65085 | -55.36626 | 2025-06-03 05:12:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70e146fa-6cc8-33ea-9595-957004101037 | -12.37031 | -54.16987 | 2025-06-03 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 77c14b2d-a4a7-3ae2-9eac-79902588f268 | -11.57982 | -47.44767 | 2025-06-03 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d3301643-18a1-34eb-ac2d-7cbfee4f8473 | -10.13947 | -52.14147 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7d4af6ea-986d-395b-85e6-2c417a24be23 | -10.23566 | -52.22952 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1ec93d55-ee37-3fd3-b349-9c3169601b5e | -12.37101 | -54.16479 | 2025-06-03 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15af0217-afd6-3ba6-ac07-463809f97067 | -13.6363 | -52.18817 | 2025-06-03 05:12:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 24c6d675-2b71-39c9-abf2-bb34cefb8e38 | -11.90434 | -47.44749 | 2025-06-03 05:12:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ec26925-5772-3b76-a730-5a4b902fb27e | -11.92082 | -54.81501 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf6cbab8-8eaf-3e5a-a54c-04d8e57d5f6b | -9.23815 | -63.29655 | 2025-06-03 05:12:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README14.md)

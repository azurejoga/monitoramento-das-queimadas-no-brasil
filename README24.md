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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f16d4e0-3d13-34e6-adda-2bc26f9cb033 | -2.58511 | -51.91917 | 2024-12-12 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd5c310f-dcb6-31cb-8c14-2fb768c32342 | -2.7312 | -47.88658 | 2024-12-12 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c038b76-abaa-3ad1-9e5c-21e9db8973ff | -3.42928 | -42.98511 | 2024-12-12 04:38:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65669ac0-49d7-360c-a377-5274e7cf77a1 | -1.59936 | -46.48484 | 2024-12-12 04:38:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c7f506f-db3d-3adf-ab17-ec44b30b4bf3 | -6.93201 | -43.53897 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b33677b9-048e-3c55-9a1b-877628faf0be | -6.12788 | -42.54729 | 2024-12-12 04:38:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 795479cd-869d-3885-af79-717b14bedc9a | -4.17032 | -48.75748 | 2024-12-12 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0796867a-21e7-3145-9020-55419114dbfd | -2.56827 | -51.88791 | 2024-12-12 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5bcd8615-174c-3fb6-ad5a-0818a760ca71 | -7.47017 | -44.73902 | 2024-12-12 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e8e187c-c02b-33b5-beb0-501cdf3292ea | -4.35566 | -49.74915 | 2024-12-12 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fba6fc5c-e689-375c-9de3-03c4e048d1eb | -7.60454 | -46.64998 | 2024-12-12 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2eb022a-3e98-3115-a934-cca5f485503e | -4.86362 | -40.75227 | 2024-12-12 04:38:00 | NPP-375D | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6fc2ea60-a0e5-36e0-a84c-36e67563e8f0 | -2.95973 | -47.89676 | 2024-12-12 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e7689555-7db9-3e7b-8a92-69de08c62b48 | -3.85396 | -40.45334 | 2024-12-12 04:38:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 51533241-3d7a-3822-a5ad-2985ed555644 | -3.15098 | -48.5274 | 2024-12-12 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c2eeba5-2644-37ce-96b6-9be7752dfb43 | -2.96373 | -41.82428 | 2024-12-12 04:38:00 | NPP-375D | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8915813a-a421-34a1-b089-c4b184157f22 | -4.01707 | -46.88785 | 2024-12-12 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a9b3920-73f8-30b6-aebf-117477b09d51 | -5.29933 | -43.27974 | 2024-12-12 04:38:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 044b5829-7c90-3d35-a48a-e9d4772f5366 | -5.2241 | -43.87764 | 2024-12-12 04:38:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f7ad56f-f3ea-37ba-abc4-7b662526624d | -3.2503 | -46.8709 | 2024-12-12 04:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 8f6caf98-43e3-3c86-be6b-9d65ec0eaa97 | -12.5682 | -57.7579 | 2024-12-12 04:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 98c6ac98-ee09-397a-84d3-d51f417693b8 | -6.9158 | -43.5185 | 2024-12-12 04:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 1bd33ee7-e3e3-32f5-9bad-07c8238e7431 | -17.2994 | -53.7767 | 2024-12-12 04:40:00 | GOES-16 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 0918f818-5eaf-3bdb-9092-445e7694a337 | -6.9346 | -43.5168 | 2024-12-12 04:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 108.2 |
| df9cf68e-8e0e-35b5-b170-bcc85f083796 | -14.7655 | -52.6446 | 2024-12-12 04:40:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 4ad3b685-4084-3eee-92e0-9f3d950471e9 | -14.7461 | -52.6471 | 2024-12-12 04:40:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 95.2 |
| ec094e72-b639-3bda-a8b6-a05689816570 | -6.9344 | -43.5401 | 2024-12-12 04:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 77.8 |
| e8bc1c76-3c3d-3a9e-9606-6e0797c8a853 | -10.02125 | -47.56227 | 2024-12-12 04:40:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9c8bf1a-8810-307a-b343-68edbeb83ef1 | -8.36934 | -44.48577 | 2024-12-12 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38e756d0-c091-3214-af46-35f5e952227d | -10.64738 | -51.77513 | 2024-12-12 04:40:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 174f5d92-6862-37f1-a00d-a9f7a8039b35 | -8.40133 | -49.17602 | 2024-12-12 04:40:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3bc6549-cdf4-30d7-be1e-915611585a9b | -11.21075 | -53.83275 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a1bed2d5-fe79-3dd8-9119-0f4b56a7d16a | -9.23456 | -46.66962 | 2024-12-12 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| efdc9b47-1623-38e8-ad01-ecabc1d6f1c6 | -12.40555 | -49.67946 | 2024-12-12 04:40:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac866f51-02ca-31ab-95d3-d79c7ce8bde9 | -10.19288 | -36.22895 | 2024-12-12 04:40:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 32.2 |
| de2bd5d3-7cb2-38a0-9e3b-ad7f1c038f51 | -12.90712 | -48.59716 | 2024-12-12 04:40:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8f60512-1179-3bcb-9b09-130cc801e1e3 | -14.74184 | -52.6407 | 2024-12-12 04:40:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7f628633-d5ab-38c2-b0eb-3529d7da5c02 | -8.36754 | -44.48577 | 2024-12-12 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 323a839b-1125-304a-b7e9-5efa4514cfcc | -13.70114 | -54.76397 | 2024-12-12 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e5678f15-5f29-37e5-afe0-d5f0c2755faf | -10.53688 | -44.6794 | 2024-12-12 04:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13bb21f5-8445-3cc8-91d7-756977773188 | -10.49611 | -44.63433 | 2024-12-12 04:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 445b47b7-4e77-351a-861c-ea214fcd50d1 | -11.19984 | -53.83092 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 726daba4-07ae-37ea-8549-835035b0cb19 | -11.11479 | -54.65232 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8bd08a12-8ed3-361b-92e2-2b2fb960ab6f | -11.68866 | -48.08154 | 2024-12-12 04:40:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acb7ea48-df49-3b11-9679-2e3cb578d8dc | -12.92265 | -55.05465 | 2024-12-12 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 78e56a8c-0527-3b76-b611-8a5ca66c3ea4 | -12.91967 | -55.04927 | 2024-12-12 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7152578-7a5a-3ddf-93cf-a6bbb9fd7052 | -12.55514 | -58.35302 | 2024-12-12 04:40:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 354f5991-3a58-3b49-bb28-363d848062bb | -8.30816 | -55.10779 | 2024-12-12 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c207c00c-da1f-3450-8a77-d8f1505e07ba | -12.07652 | -48.39957 | 2024-12-12 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b749fc1-63a8-384e-9c55-7cd39f52fb5e | -12.91588 | -55.0486 | 2024-12-12 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f1dedd1-f40e-3348-99b9-f5271073fe0d | -10.01178 | -47.55264 | 2024-12-12 04:40:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1267a98d-cb5b-3806-a039-c228caab0b7c | -10.49516 | -44.63685 | 2024-12-12 04:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9928074f-faf8-3001-9db9-4ae7d14d6238 | -9.79059 | -36.21893 | 2024-12-12 04:40:00 | NPP-375D | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5e519a12-ff34-33bd-b16d-48d1624adb4b | -9.60021 | -49.52677 | 2024-12-12 04:40:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45f54079-e2a9-3f6a-a635-a0ec04c25c8f | -11.20924 | -53.81941 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a8a7aec-112b-3131-ab21-7a000282dffb | -9.39115 | -38.88035 | 2024-12-12 04:40:00 | NPP-375D | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| aa918907-ec09-30d0-9144-83c354e0f0a8 | -12.91804 | -55.05869 | 2024-12-12 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90e9ad9f-6a45-374d-99ae-7476b66e1764 | -11.21146 | -53.8285 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d73cdf92-7cd7-3bdd-ad90-69fd16679e61 | -9.59687 | -49.52624 | 2024-12-12 04:40:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d8a2232-d8bb-3355-a97d-360f9c33505d | -9.19624 | -49.47407 | 2024-12-12 04:40:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd12d216-a310-3bf4-a76b-263637801b8d | -11.87788 | -43.71962 | 2024-12-12 04:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f1f91ae7-066f-30fb-99bb-0f2af4fe6f04 | -10.87747 | -54.32161 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e192ae4c-981b-395b-b983-65bbbf7742f9 | -12.53699 | -57.74054 | 2024-12-12 04:40:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7dcd0629-3a78-333a-b805-b7b7a6f641fc | -9.78968 | -36.22635 | 2024-12-12 04:40:00 | NPP-375D | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 6cea5aa0-c4d8-3e7c-afbf-53eeefd32d41 | -13.69377 | -54.76262 | 2024-12-12 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4934a9bc-56e8-3206-bb35-5b23116ac086 | -10.02185 | -47.55826 | 2024-12-12 04:40:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1c99e8f-17bd-3255-9acb-96acde4b056c | -10.55488 | -44.58092 | 2024-12-12 04:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 53933542-3f16-322b-a94b-06b181003ff1 | -12.91506 | -55.0533 | 2024-12-12 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0050b42-727e-390f-8196-43fa086379da | -11.70967 | -57.35526 | 2024-12-12 04:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dfe6c51c-98d2-3bc2-95d4-13648628c9a5 | -10.19932 | -36.23724 | 2024-12-12 04:40:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 32.2 |
| d0357435-5fd8-352f-a527-2615f701c7e0 | -14.74701 | -52.63028 | 2024-12-12 04:40:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c00197ae-e146-3d11-9ff9-e04f5160f442 | -11.20205 | -53.84003 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| eb1e5944-0af1-3872-ad25-9bad35152378 | -9.20232 | -49.45697 | 2024-12-12 04:40:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0631233a-b1ab-325f-811d-179cec371d7f | -10.5448 | -44.68451 | 2024-12-12 04:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e47de208-af23-3a51-98dc-8eba29c1d03c | -13.06822 | -52.04265 | 2024-12-12 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 533b2137-3d68-3b89-97b4-ffeabcf53b70 | -13.65501 | -52.93937 | 2024-12-12 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e7543d3c-fbb9-34ae-ab9d-7aeebcd3a197 | -10.454 | -45.06232 | 2024-12-12 04:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9168b2d0-3cf0-31a0-9e51-b059a6877fbb | -10.54111 | -44.68 | 2024-12-12 04:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3d48b0ac-7503-39fb-a60f-7ca73ab4953e | -11.20419 | -53.82728 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a64743bb-5fb0-3c5b-ba2d-9356963f8557 | -13.32241 | -52.41015 | 2024-12-12 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6e517e4-246a-378c-ba63-43576c484645 | -8.62318 | -50.02149 | 2024-12-12 04:40:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 304d8f24-a5ef-3f6f-8bc4-a3e0e92512d7 | -10.35002 | -57.25084 | 2024-12-12 04:40:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dce28c65-c1c1-3635-a456-af3efb050c88 | -7.56914 | -49.40533 | 2024-12-12 04:40:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0f3d812f-8ffb-35e7-a434-0f664ab43c80 | -11.97107 | -49.12038 | 2024-12-12 04:40:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa0298fd-e891-31bb-a563-e0c173a3b0df | -12.92725 | -55.05067 | 2024-12-12 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 440d4e37-3e00-3494-bfeb-5501be8fa299 | -9.19569 | -49.47759 | 2024-12-12 04:40:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3645f5d2-9f46-3636-9087-17ac9c36bb6a | -8.36518 | -44.48515 | 2024-12-12 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc11ec21-ec80-3424-bd85-3d1102797bb7 | -9.37709 | -57.55174 | 2024-12-12 04:40:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef9f0281-ca8f-3fdf-aba3-7054c7bb99d5 | -11.48179 | -48.21388 | 2024-12-12 04:40:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f800b923-1983-3901-80e2-4c98f904505d | -12.9171 | -55.72981 | 2024-12-12 04:40:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68f733f6-9ff3-3d57-8f23-1024705e9d8e | -14.74581 | -52.63759 | 2024-12-12 04:40:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5713b41d-17c9-3e5b-950c-f76cfde085b5 | -10.77643 | -51.9272 | 2024-12-12 04:40:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a808020-bfec-381b-9010-9d9331ee901c | -10.20034 | -36.2243 | 2024-12-12 04:40:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 28.3 |
| 765c0953-8d2e-32d2-82bf-e705bf8724b4 | -10.20187 | -36.21476 | 2024-12-12 04:40:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 85a46279-607d-359b-84ac-0a9635d036cf | -8.62373 | -50.01801 | 2024-12-12 04:40:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb519bdb-b06f-3aae-b559-c6cfce2ecb96 | -10.53633 | -44.68332 | 2024-12-12 04:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e6d8f45-e6bb-3c8c-8f79-07058c4f239b | -13.06151 | -52.04153 | 2024-12-12 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 597d1e94-ce4d-37d3-9420-1d49a6701d3c | -14.74461 | -52.64494 | 2024-12-12 04:40:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0d29dca5-855e-3b8e-b348-d7439c9db7dd | -13.69746 | -54.76329 | 2024-12-12 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7c0ebc5d-1a03-3f8a-85dd-2c84674dd588 | -8.69378 | -50.19354 | 2024-12-12 04:40:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README25.md)

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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd9a8c0a-7f00-3086-b8b8-a7f881cbda7e | -11.78853 | -46.64711 | 2025-09-14 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1de08cb9-ebb0-38bc-9054-344c905103b7 | -10.59829 | -44.33901 | 2025-09-14 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6d51103c-cf9a-3a0b-a404-e9bdf7f03f16 | -14.37212 | -52.93587 | 2025-09-14 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37656b35-c051-3c9d-a3b6-5039f4562584 | -12.91661 | -54.74954 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 816a2e89-4014-33cf-98ea-651f576d403f | -12.95332 | -48.03656 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f24c195-8892-3852-bfbb-be60a5b9962d | -12.67898 | -54.67863 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bf6243ab-d33d-3540-976d-01353b3aa924 | -13.94494 | -44.84088 | 2025-09-14 05:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| ae635c44-ba44-33c8-8e9a-a3714182e17e | -12.93176 | -47.9457 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4812b493-cf3d-319a-91cb-7077deca82d7 | -14.62074 | -52.02518 | 2025-09-14 05:08:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c3d43f94-cddb-3909-a605-646f98b6d707 | -14.31536 | -46.08992 | 2025-09-14 05:08:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9227170-e517-3ea3-9aa6-7317fb099f72 | -12.77895 | -48.01973 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7059075c-1b90-31ea-bc5b-e327ef77deaa | -10.73818 | -46.43862 | 2025-09-14 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b087436-67ed-3acc-89ab-52ffaef98fb8 | -12.97065 | -48.0285 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70bc5cfd-35af-31ce-9ce5-a936c9617edb | -11.27461 | -51.11294 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cbebec55-6d80-3005-b671-d61a8ed729e5 | -11.77891 | -46.62934 | 2025-09-14 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2c622673-be7f-3d8c-9a5a-c15d8d7fa2e1 | -12.69246 | -54.68481 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| cd198e67-2172-3645-aa54-4ed023bfb777 | -10.88861 | -48.17921 | 2025-09-14 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7460f77d-845d-3f3c-a8f2-d1c16001dc7c | -12.86128 | -52.97908 | 2025-09-14 05:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 44342c47-396a-3322-afe0-981c78870040 | -12.78389 | -48.02381 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 61a6483e-f49d-3ab7-aa62-b1198e8ec942 | -12.66196 | -54.67198 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a247334-927c-369d-961a-559ae5b7dedf | -12.68072 | -54.69118 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 54eec8f7-a6ac-3c97-8ac0-59946c6f71eb | -12.6696 | -54.66906 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23c18595-c8c3-3ca3-80f9-15ed15661c31 | -12.66078 | -54.67999 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| a4d50d1a-d88a-39c3-98ce-c470f5761035 | -11.8517 | -50.48932 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| ebfdaaa0-f19e-3ca3-a4a7-420eb326dc11 | -11.1449 | -45.32293 | 2025-09-14 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c89d1a8-f66b-3220-90cf-6671e2cb3429 | -11.38716 | -47.34171 | 2025-09-14 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ad9e0218-ac97-34a9-ba90-b8b26c3b7ce9 | -12.69062 | -54.72125 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 329be84e-5a55-3450-a4d2-a1e6ecdff36d | -11.3706 | -47.34031 | 2025-09-14 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36c9e588-03a7-3945-a6d4-30ca7f96ad40 | -11.78243 | -46.65026 | 2025-09-14 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d05fff5b-1588-365e-b481-eb43fc3e2410 | -12.87018 | -62.10053 | 2025-09-14 05:08:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 61ced68c-2b25-3226-aef5-76b69f260b34 | -11.4602 | -48.70154 | 2025-09-14 05:08:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5af0dec4-187d-341f-8930-e816fe656446 | -11.82764 | -50.49949 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 8c7c3ba0-414e-3c38-ac0a-b7d1849076ea | -10.91904 | -47.19583 | 2025-09-14 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37af90e6-6351-37c7-9cdb-5f88894faaa7 | -11.25156 | -44.76467 | 2025-09-14 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| c8c96112-162a-3a93-9835-8e7aae9df077 | -12.04755 | -46.54487 | 2025-09-14 05:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 509a38b2-ed4c-3658-b3e2-3b0e069bbc38 | -11.37953 | -47.71167 | 2025-09-14 05:08:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2419213a-6139-3b34-bd22-d92c5a789058 | -13.89787 | -48.30528 | 2025-09-14 05:08:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 847f2907-de69-3fe5-a082-5f8b1de0591d | -10.89429 | -47.2145 | 2025-09-14 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c23b853c-7160-3d25-95f1-6d3c3a27a285 | -11.46362 | -50.75324 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d1409488-1869-3e8d-b852-998c077b609b | -14.82365 | -48.76759 | 2025-09-14 05:08:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4dbef30b-39f9-3060-bc3d-05364330dc90 | -12.65492 | -54.67088 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4695f5fc-35b0-3943-8d2c-39cc70a5af94 | -14.36498 | -52.93861 | 2025-09-14 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72ea6bc3-714b-3c32-99fa-e84231d0f3d5 | -11.81568 | -50.49899 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3de0d05c-49d6-3d4f-b9cf-43fbfe3269af | -12.78224 | -47.99224 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f27983dc-c0d7-3da2-8063-bcd522fa35a6 | -12.78689 | -47.99883 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4e3b3623-b242-32f6-9a9b-b44cc1d4bb55 | -11.78901 | -46.64306 | 2025-09-14 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 63cb771f-9a8d-339d-9a4f-fd1ed5f2ba8f | -12.97401 | -48.00164 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0bc061e2-dab3-3377-bf34-f1e78ecdcd23 | -11.47023 | -48.70285 | 2025-09-14 05:08:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 97885fe6-bde9-3b6b-8b9d-0efe5f4d8adf | -11.27572 | -51.10501 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67cb3ada-1ed5-30da-81db-b035a1e475a3 | -12.92945 | -47.96472 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26a7c3ce-3809-389d-a2fe-c8e82eb10e85 | -10.75554 | -44.78276 | 2025-09-14 05:08:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3aea7773-863b-3947-a7f4-d64fc0101f67 | -13.90863 | -48.30575 | 2025-09-14 05:08:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35d2e94e-c00c-392b-9714-d4805ad8d554 | -12.6772 | -54.69065 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 483c1cac-f340-34bc-a277-2270ee90e379 | -12.78349 | -48.02713 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7a0d1bd4-44a8-30e7-a870-38f3c8b9abf3 | -12.61365 | -57.00546 | 2025-09-14 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a23ef340-0685-3382-844c-cb6d45d56713 | -14.39992 | -52.90856 | 2025-09-14 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a537dfb-e5a7-3737-be36-893d206493c4 | -14.1794 | -54.0533 | 2025-09-14 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2904c0b2-70c4-3e50-9333-37c49ea8795e | -12.75637 | -47.99997 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c033fe1f-e797-3172-af52-c6a05e1a23f2 | -10.32562 | -48.82231 | 2025-09-14 05:08:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 470bcafd-0f89-37a4-b0a9-927dcf92fb91 | -13.01634 | -47.99118 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0500a977-dbb7-3791-b641-4c4f6d64b707 | -11.44967 | -50.78753 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 954a86a3-b622-3150-bcd7-c83ca924ce71 | -12.68596 | -54.70429 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 52e88626-dcb8-38f6-ab86-3708554bd492 | -12.93632 | -54.73912 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4a70b30e-8906-369f-89eb-805b1451f0d0 | -11.81814 | -50.48124 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 68f1ea88-8955-3e2b-b76f-754d01c2a016 | -9.97314 | -55.04143 | 2025-09-14 05:08:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b84c10b-e6de-3e4b-b6e5-3eeb674e3877 | -12.78682 | -48.04455 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c7399617-0cf5-3390-9149-4db258fb5176 | -12.9172 | -54.74557 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c639e58c-e91c-31e6-8247-6ebf1a79f67e | -13.94076 | -44.81725 | 2025-09-14 05:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e203bec-319a-332b-8a76-f0303a44ebbb | -12.67839 | -54.68263 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 5089e377-36d9-39c4-9076-1e04fa9d973b | -11.88522 | -50.54364 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 29ed1ac2-20c2-31d2-8791-0fbad825bc90 | -13.0167 | -47.98817 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c04984ff-315b-3927-98f5-1947ed2603f0 | -12.78623 | -48.00435 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 78f67f76-9a65-384b-bff5-d126aea80b1c | -13.90081 | -48.30638 | 2025-09-14 05:08:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10e4a785-7ca7-30b4-9877-59d1afb49860 | -12.85823 | -52.98125 | 2025-09-14 05:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f65a10d-9967-3804-9388-48819343e5a8 | -12.77855 | -48.02304 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| acce93ec-e281-36ee-8653-e3df2018500b | -12.76539 | -48.01472 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5adf97fd-14b6-371b-ba28-5af6692043e0 | -9.01516 | -47.04609 | 2025-09-14 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 216fa701-f3ef-3dc8-89ba-b328238b35c3 | -14.43517 | -43.2039 | 2025-09-14 05:08:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c39fca26-8c56-3f59-9909-600b6ce569b5 | -11.78546 | -46.62624 | 2025-09-14 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 973459a8-279d-38da-a768-567821c445d8 | -12.14393 | -47.58367 | 2025-09-14 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6748315e-b31a-3bc9-9fde-b96d7f3ed3ad | -11.67032 | -46.5073 | 2025-09-14 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 807957fb-0245-39ec-a733-42e5e4daa3b9 | -12.69306 | -54.68081 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 98344288-0fcb-30c1-9c6c-c2627635f16f | -11.86925 | -46.76251 | 2025-09-14 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b7166d1d-1e20-30fc-ac7c-0862fbf3d93e | -12.68418 | -54.71624 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 9c3169c7-9011-31eb-904d-74bac72a7a4c | -11.45802 | -50.79526 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 17f8e389-758a-34c4-9ef3-f88874e958c6 | -12.68715 | -54.69628 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 1ef6bfaa-29fe-3f90-974f-2b1544450241 | -11.89087 | -50.53545 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 99333580-8c06-3eac-83f7-10f697b3e283 | -12.91309 | -54.749 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b4c9261c-700e-362b-aeef-7fe9a73ac406 | -12.68477 | -54.71226 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 871cc1dc-6179-3f69-8fd8-0d860e0e2d45 | -12.10033 | -44.8616 | 2025-09-14 05:08:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d4825c28-670f-3ae0-bcb6-6dda6b59bc26 | -13.88328 | -48.29187 | 2025-09-14 05:08:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5775156-4af2-346d-9a9e-a8f22a34109e | -10.93774 | -47.35344 | 2025-09-14 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a04bc39e-d4a9-37e9-8bf9-9fd9a95aa426 | -13.93229 | -44.83364 | 2025-09-14 05:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 38.5 |
| d79fde40-ea70-3253-a01e-4dadd6903c8d | -11.82137 | -50.49074 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 29ffaa1d-2523-3365-acf9-dfc025ca4031 | -12.96896 | -48.04198 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 325b36dc-7865-3bbb-8d22-448991edb59b | -11.82881 | -50.49062 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 624d80bb-aa36-3370-a9e6-77b4edbceb5f | -12.86677 | -62.14302 | 2025-09-14 05:08:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7e0fbf9-5a9a-342f-919d-cbc10952b97b | -14.17768 | -46.15414 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd364328-1936-34bd-8037-5861aff8238e | -12.7797 | -48.0304 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c29049a-4dfd-300f-a2e6-eb8419ad3373 | -13.93651 | -44.85685 | 2025-09-14 05:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |


[Clique aqui para ver as próximas entradas](README60.md)

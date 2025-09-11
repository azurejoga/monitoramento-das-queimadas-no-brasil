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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a62c1bb-40e4-3bf7-ba7b-0254a48d481e | -16.48866 | -51.98174 | 2025-09-11 05:38:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5790c283-9a31-3e34-9e6d-e207fea13afe | -12.94592 | -54.81643 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cc57d75b-1f17-33c9-b680-ccd37734af5f | -14.93061 | -55.9444 | 2025-09-11 05:38:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d45d0c4-b97d-3540-8ef2-4fd2117f0de5 | -11.05816 | -51.33882 | 2025-09-11 05:38:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| aa38156f-3fbb-3c18-bc22-255d5d3e32df | -11.22441 | -55.00132 | 2025-09-11 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f7b177eb-1080-3f04-9b4a-496fd7881539 | -13.2241 | -51.76723 | 2025-09-11 05:38:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d39507ca-2471-3a35-b558-9f415019f0a4 | -16.5365 | -55.17547 | 2025-09-11 05:38:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| f649e994-7f0b-31c4-8100-c56a5d13d4ae | -12.92273 | -54.75808 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ecbed26-88e1-31e8-a9f9-d82c0803ea31 | -15.56399 | -54.74814 | 2025-09-11 05:38:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| aa9b5298-6e64-331e-b250-cad6645cebc8 | -12.0649 | -64.17116 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db64c702-a04e-3784-84f6-fe45d8211173 | -14.50875 | -53.95835 | 2025-09-11 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2504e926-ef6f-319c-9e2c-d361bac4e782 | -8.88909 | -70.60728 | 2025-09-11 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a8c4ef7-f93a-3e06-acc4-f9e3085dfbf6 | -10.00582 | -51.71922 | 2025-09-11 05:38:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6f26a9e3-f994-3829-a42c-d84142859a15 | -14.28693 | -54.74209 | 2025-09-11 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5e2858c9-39e2-32e9-abac-0317202431c2 | -9.983 | -64.98634 | 2025-09-11 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd81c8e8-8149-3d5e-b1a2-4b7fc643874a | -14.885 | -55.85086 | 2025-09-11 05:38:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 119dc200-2edb-3823-8adf-9d5a948f6f36 | -9.79322 | -61.51658 | 2025-09-11 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9be1e402-b327-398a-b026-537961cbc55d | -12.9295 | -54.80098 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de4614db-abb5-3b37-b131-edd3b5671545 | -11.87474 | -58.81367 | 2025-09-11 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cd3a1282-ec83-3be8-8935-194c5a9214d9 | -14.30917 | -54.75779 | 2025-09-11 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee94ab06-61ca-3c34-ba30-f2ecb885ae9f | -12.38368 | -54.17528 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aa07edaf-77c6-328f-b569-1078edbcd3c3 | -12.60489 | -56.96815 | 2025-09-11 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 657d4098-a8b1-3f78-ae4b-cbda9cbce7f1 | -14.88805 | -55.87409 | 2025-09-11 05:38:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 45d77807-cc0e-3daa-a210-391b53879649 | -9.80841 | -61.52657 | 2025-09-11 05:38:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e4deaec2-c4d8-36ed-89c5-72ab32497e62 | -15.80672 | -52.22645 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 72daa84c-5e72-32bb-842f-7ca643b1ec49 | -16.53606 | -55.17987 | 2025-09-11 05:38:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b0a4459e-df97-3594-8014-19344d9d5797 | -15.55553 | -54.77094 | 2025-09-11 05:38:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51065581-5578-3b87-aca9-7c026cae1db0 | -11.77619 | -64.93934 | 2025-09-11 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f8abbb8-632f-3d23-8238-c82058b10d58 | -12.39466 | -63.81644 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 852cdc07-be0e-3907-8250-09b2de7f1f06 | -12.85633 | -52.94747 | 2025-09-11 05:38:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1d17dd81-4592-3c2b-983d-3ea1c7871c16 | -12.41127 | -63.81099 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5fffaa9a-5517-37a7-abb2-881a536b1eaf | -13.13441 | -54.91704 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 66f656f3-45eb-3796-befd-cbe1f19e17ac | -17.37532 | -52.93984 | 2025-09-11 05:38:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| bba3e05d-b798-3cc5-99ea-308c3dfa701b | -9.9863 | -64.98686 | 2025-09-11 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46c26f92-6e06-3d7c-bf9d-a60a7c1a4075 | -12.3938 | -54.16533 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c84b424-f474-3b20-99e7-ab395e9133b2 | -12.41017 | -63.81829 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8b68e2e-fab8-3351-8085-7353b3890a1b | -11.22293 | -55.00256 | 2025-09-11 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0ea5bed1-2d8d-36f7-8661-2601b5dca686 | -12.93046 | -54.79278 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c99dd237-785f-3534-b82f-5b83e3db2317 | -16.53801 | -55.17758 | 2025-09-11 05:38:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 7d2906ab-57df-3f92-ba74-3d7841aa2e86 | -14.31014 | -54.74905 | 2025-09-11 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad3d6945-e79d-3753-925c-75331496e403 | -12.61059 | -56.96305 | 2025-09-11 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 952b3aa8-4eae-3c66-8ca0-4acbcb27f255 | -9.61766 | -67.34162 | 2025-09-11 05:38:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0bd575a5-00fa-3e9f-baf8-e0473806caee | -14.91058 | -55.8737 | 2025-09-11 05:38:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07568ae6-e2e8-3e41-90d4-fcd2e5762aa1 | -10.00649 | -51.71328 | 2025-09-11 05:38:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 72cf03cc-4641-3f5e-bee0-c2db348f33cb | -11.78444 | -64.92989 | 2025-09-11 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c4b087d-d33e-3227-8612-424e33fde5cc | -10.4653 | -67.83519 | 2025-09-11 05:38:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca8aa3da-0b14-35e7-b5cf-82274dbba06d | -14.88622 | -55.83982 | 2025-09-11 05:38:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e522556-dd70-31b3-985f-c326a825e2f9 | -9.84886 | -64.99641 | 2025-09-11 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d8e8347-4aed-3401-b5b4-9ccf5cf4297e | -15.81361 | -52.22842 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 32ecfc48-0f15-3c52-9f68-5af7c318956e | -15.11807 | -52.40876 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 51a73fd5-1f44-396f-abc7-dfc9f836308c | -11.88407 | -58.81034 | 2025-09-11 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ec83dc3f-e825-30c4-bb6e-740dc5ee5d54 | -8.94996 | -64.28208 | 2025-09-11 05:38:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c143d3f-f379-3660-bfe1-2c13f016a67d | -12.95378 | -54.74485 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9aa294f1-6bc9-37f1-9198-ccb06d137c62 | -12.60525 | -56.96521 | 2025-09-11 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac1d0e73-7860-3d15-96c0-d323f734bec6 | -11.77949 | -64.93987 | 2025-09-11 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76f231a4-d3f8-3f53-ba53-22070d47cbe4 | -12.9596 | -54.74556 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4a3c8c1c-ba64-38e0-867d-985f187dd52c | -12.92998 | -54.79684 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 790926a7-d707-310c-b442-f0277263bd1a | -12.96401 | -54.75974 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3d6b0376-4fdc-3bcf-a85a-3760a046d45d | -12.06823 | -64.17168 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8d3d6194-920c-3e0e-a462-1d1ba52afcb6 | -12.92177 | -54.76629 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aa57cc60-1aaf-3317-b8b8-630b8c6d7d01 | -15.1707 | -56.35148 | 2025-09-11 05:38:00 | NOAA-21 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| aa961318-a6aa-30d2-869f-8de09b8576c6 | -15.17029 | -56.35505 | 2025-09-11 05:38:00 | NOAA-21 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8e565e0f-1048-3b74-a2ed-686bb9c4db26 | -15.79924 | -52.23083 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 192da6cc-3ca4-35e5-bb11-fdb66fdda4e3 | -12.40399 | -63.81361 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf2b28dd-76a6-3aff-971d-0b3ac181bc9c | -9.80901 | -61.52239 | 2025-09-11 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86be0ce4-1086-30c7-9163-82bc9ef893fb | -9.79743 | -61.51296 | 2025-09-11 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7f8445f2-7e39-35a8-b585-7eab7a39df5a | -15.87415 | -54.93368 | 2025-09-11 05:38:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0c5743b0-3cdf-358c-9f78-997ae53629bf | -12.39744 | -63.79818 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc67ee90-8fad-31ca-a696-328053c01951 | -9.9797 | -64.98581 | 2025-09-11 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56eb70aa-31a0-3b60-be1f-2669e59eb460 | -12.86282 | -52.94831 | 2025-09-11 05:38:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e51be263-d12e-30fd-91f1-2beddf850188 | -9.25234 | -63.51683 | 2025-09-11 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 968810fb-ff56-3b17-a559-e40416b8bed5 | -15.16049 | -52.40912 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 91e4130f-072d-3399-b504-5448c102869f | -15.15917 | -52.4229 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ee98a977-4dcd-341e-aeb5-c3ad015ab55d | -15.13523 | -52.44517 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 11527dc3-8c13-3620-8d1d-9a6d8e8a77e3 | -12.9459 | -54.8115 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dfcb23aa-82e2-36d6-8360-b305af73c143 | -15.12488 | -52.41026 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1f9fca74-7b9a-36c1-9310-c99d2fddce86 | -11.22854 | -55.00317 | 2025-09-11 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8973dcb8-23a2-30f7-b9bb-4d15189c5f94 | -12.92902 | -54.75475 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9fc5771f-6666-3a62-9001-324471095e80 | -15.55005 | -54.76525 | 2025-09-11 05:38:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e0a0c9f-7e27-34cc-9dbb-3a9d023d75fb | -12.06877 | -64.16811 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 576d495c-b55c-313e-bbe9-ae822decabf8 | -10.00513 | -51.72532 | 2025-09-11 05:38:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 29260936-6fb2-362e-9140-6b4cb2449cf1 | -11.16147 | -57.18162 | 2025-09-11 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ecccf1d9-cdb2-3854-a9e1-5d77902b6bc4 | -10.1129 | -64.91772 | 2025-09-11 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1e9b694-f385-3e3f-b2b9-729622e267d9 | -14.50412 | -53.94275 | 2025-09-11 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7062dcad-e449-3f39-8b97-a7556b910eff | -11.15368 | -52.03465 | 2025-09-11 05:38:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 27c39454-60a2-31e9-986e-01bb274a3d21 | -13.1903 | -51.76484 | 2025-09-11 05:38:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2bd66545-75a5-3d74-8497-44f084e8721f | -12.96492 | -54.75048 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0b13f7e1-9f31-3a35-84c1-7bf89cd56df4 | -10.33583 | -54.54956 | 2025-09-11 05:38:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b19f2ca1-f2c2-3cd4-bb54-d4402ce52de6 | -15.13098 | -52.42687 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5ced74eb-ec6f-3ab2-a6c9-6460837de61b | -9.78765 | -64.88673 | 2025-09-11 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f420321-dead-3a7e-8640-0c44d07cfb66 | -9.78435 | -64.88621 | 2025-09-11 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 201b17cf-9b5b-3d7d-83c7-2c4f1217d83a | -11.88731 | -58.81927 | 2025-09-11 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de7f57f0-7ffb-370d-93d2-0fd1334fde2d | -12.07047 | -64.17934 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dc5339a1-82e7-362c-a34e-b58a4215a059 | -10.46888 | -67.83578 | 2025-09-11 05:38:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3333be5-98ee-340f-aa2b-f3ccf4bce067 | -9.84555 | -64.99589 | 2025-09-11 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e4c7461-b6ec-37dd-88d2-636c8fa806d8 | -16.54247 | -55.17569 | 2025-09-11 05:38:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| c303c7aa-237f-372a-b188-25cbb0519410 | -9.79978 | -61.52183 | 2025-09-11 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| db1fb242-7472-3093-a6ba-2ab4acc16208 | -11.79377 | -62.73526 | 2025-09-11 05:38:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 221a9d51-ce64-3840-8e8a-b3a10a93ae8a | -15.1299 | -52.42924 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e78ae6e1-4aa7-330f-925c-2617ee6cb9f5 | -14.88539 | -55.84733 | 2025-09-11 05:38:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README127.md)

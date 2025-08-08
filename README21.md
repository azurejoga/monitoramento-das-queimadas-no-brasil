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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dfa9f3b3-7c83-31fb-b547-bc0d1b0a529b | -13.8964 | -51.84086 | 2025-08-08 05:01:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5033f160-1b6c-3ea8-9d4d-a5f93b40cd06 | -12.52161 | -47.11852 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ebfec617-6662-3b5c-8528-c076be0b0118 | -12.30872 | -50.0044 | 2025-08-08 05:01:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28670c1a-8b8f-3b49-907f-8576465a2b0a | -9.70219 | -61.30126 | 2025-08-08 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4a3139f9-adad-3f46-b314-155b2b47b943 | -9.71501 | -62.40605 | 2025-08-08 05:01:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9f1dbd05-ce8d-341f-a8fe-95b1363adaf6 | -14.36028 | -51.10634 | 2025-08-08 05:01:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 79dd7dca-1a4d-38fc-b5e7-8237ee9f798f | -12.52123 | -47.12145 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1002eaa5-af09-3221-a2ef-f6dcbb35f56d | -19.12536 | -43.51368 | 2025-08-08 05:01:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5ef2e34a-b53e-3f81-a115-16bd9b1b11a7 | -9.71436 | -62.40952 | 2025-08-08 05:01:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 541f942d-150a-3505-95bd-c9207351f090 | -13.04684 | -56.86281 | 2025-08-08 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb35df6c-5ada-3e80-84d4-3d40cbe5d918 | -11.20027 | -51.43831 | 2025-08-08 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19c50273-6c48-3cf3-9333-c392da636cb4 | -11.74772 | -47.51667 | 2025-08-08 05:01:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d92fdeda-ab91-3c6c-b7f5-2e773801ec06 | -9.94123 | -60.46768 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2bd48fd5-87e9-3dd3-8b9c-db2c567744ed | -14.81289 | -48.41033 | 2025-08-08 05:01:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be3e1ac2-bb34-34b8-b32a-545f02e29e4b | -12.55399 | -47.13872 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 15f5f9ce-9b62-3fa7-a91f-ad7eb3400bbd | -12.52353 | -47.10373 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0466b49d-8834-317f-84ae-71b93223b8f4 | -12.09577 | -44.73391 | 2025-08-08 05:01:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d13a51fb-f483-3a57-9ca5-795b838540ba | -12.54339 | -47.14134 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ace35737-a502-3081-94b2-191c0fd27585 | -11.74554 | -47.51337 | 2025-08-08 05:01:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 54822c1a-6749-3d16-8111-d3e078ef3729 | -12.57577 | -47.16962 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c1b7254-0649-3916-8ebb-77474c5778c2 | -9.94189 | -60.46384 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0e4da03-71a6-3f5a-a055-e3d8b14b4738 | -9.93727 | -60.49068 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c39619b-0d19-3b7b-8516-95ff7f4dea77 | -11.31889 | -55.21989 | 2025-08-08 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c16ce524-7528-3f09-a4c9-72fc066707f9 | -11.19653 | -51.43774 | 2025-08-08 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e262333-02c8-3be1-b91a-300f2ad19f39 | -9.93026 | -60.48147 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a2d019f-488d-30fb-957b-4061b0ec2236 | -9.71027 | -61.30728 | 2025-08-08 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a38efef7-1701-3404-b9c1-8a7c7a496695 | -19.22428 | -46.58507 | 2025-08-08 05:01:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 670cb047-8445-3376-ba86-ddc4240be0d2 | -11.74071 | -47.51242 | 2025-08-08 05:01:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c86001cc-965c-3d0c-8489-2651ca03b88f | -11.76697 | -47.50082 | 2025-08-08 05:01:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f331bf9e-c024-375f-ac7b-1a881e89cd6e | -9.703 | -61.29065 | 2025-08-08 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 650b337c-d2c1-35fb-b3b5-a0e2782bf9e8 | -12.52375 | -47.13407 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9d94b7e8-05db-3fd8-84e6-af4ce6953dcb | -9.93244 | -60.49374 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9df5c726-4189-3434-a538-8abcd89d71de | -9.71546 | -61.29743 | 2025-08-08 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f379a93-38e1-3bc7-8a29-9d141c0ce8ec | -9.92761 | -60.49681 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 916bc8cb-c803-34e5-a1f4-72d41dc2d41c | -9.93773 | -60.46311 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 858911e1-42ab-33d3-988b-b49408036260 | -9.70585 | -61.30011 | 2025-08-08 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 285176a9-b7e7-3c3c-854a-7bbe236920ee | -16.364 | -53.33961 | 2025-08-08 05:01:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f000135b-79c0-3e08-a7ad-ace279baf170 | -18.91726 | -47.55672 | 2025-08-08 05:01:00 | NPP-375D | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b3a99a80-9225-3457-a4ac-de06f2991ebd | -11.19948 | -51.43988 | 2025-08-08 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cc193371-6298-3659-8ecb-4cd5e61c6107 | -12.58007 | -47.17615 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fcead17d-d82f-3586-8f1e-e855f12fc2bc | -9.71102 | -61.30291 | 2025-08-08 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2dcdb4af-d70e-32ae-88c5-8cdc72ffd4fe | -12.52086 | -47.12437 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eac11480-a682-3469-b4d9-56b38d8c9c25 | -11.77612 | -47.50681 | 2025-08-08 05:01:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 11241d0f-8910-3f70-abc1-92ccf3334736 | -12.58585 | -47.17099 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3327fe58-3d56-3548-9e65-a9b131f9c05c | -17.61552 | -46.7136 | 2025-08-08 05:01:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f37b04a1-5020-30ce-a9a8-d5ed1ba99a5e | -14.7375 | -46.30362 | 2025-08-08 05:01:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18f07639-5fa2-3194-a76d-015b6da0b2dc | -19.13175 | -43.51975 | 2025-08-08 05:01:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9ed3981d-0123-3292-86e1-125fda54d8f7 | -12.58082 | -47.17029 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d89c7100-b7bf-3b79-9c4f-09047b12de1c | -13.03893 | -56.86896 | 2025-08-08 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aaa8bd3d-ae5c-3231-bbe2-ef2f58b8c882 | -12.5232 | -47.13853 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2c420a22-0e38-35e3-b769-1e7987e44a0f | -9.71618 | -62.39925 | 2025-08-08 05:01:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b7082c5-dd32-3d15-946b-9b836b44ed1a | -9.93311 | -60.48989 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90f59a67-a435-330a-919f-849abff9e7dc | -13.04288 | -56.86588 | 2025-08-08 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cec21e97-3571-35d8-82a9-1cf5a0134ca6 | -9.70506 | -61.30446 | 2025-08-08 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 45d6d729-a2fe-3082-8093-2a336f59b8bd | -9.71388 | -61.30613 | 2025-08-08 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 87303851-30ce-3ca0-b0ea-7eb29535a4b4 | -12.54009 | -47.13451 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 89fb1b35-2ecf-3560-83a3-a3e8efc81af1 | -9.92592 | -60.45693 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12e8611c-a458-3f63-b613-5e4dd7a42a87 | -11.75038 | -47.51427 | 2025-08-08 05:01:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a64c350c-53e1-3662-a73a-520dce97af4f | -12.61581 | -48.10961 | 2025-08-08 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 430fffbb-8d74-35ae-bdb4-0bf80d7a878b | -12.52248 | -47.1444 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6d2bba55-0764-315d-a736-4ab2088f36c3 | -13.0423 | -56.86952 | 2025-08-08 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f8ee1a7e-c8d8-3f74-ae6f-69e1f1812398 | -14.8135 | -48.40532 | 2025-08-08 05:01:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 171aae57-e153-3639-8078-2603407826cd | -12.53384 | -47.13549 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 35150f40-a3d6-3184-b771-64cf3fa9e27f | -9.70742 | -61.29145 | 2025-08-08 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ba2631db-0553-3c05-bb0e-2727658094cd | -11.1896 | -55.01205 | 2025-08-08 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c1f320d-70e3-3abc-b7b8-155a920926b2 | -12.522 | -47.11558 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9bedda9-6739-3fc9-b4b0-8f64d94e8cb4 | -12.5333 | -47.13992 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| aa29081c-3f65-3be9-b729-f4dc71fa7354 | -13.0508 | -56.85973 | 2025-08-08 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a94a35f-ff44-3a1d-90ec-604d31133baf | -12.52342 | -47.14423 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b9d1eab7-87fa-32c2-89a2-0bf0fe13ec63 | -13.89706 | -51.83618 | 2025-08-08 05:01:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5670b9e-3811-3adc-b5e4-872a87cf7df7 | -14.73708 | -46.30721 | 2025-08-08 05:01:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1545e2ee-8ff6-304d-9367-3e7595756c69 | -16.3634 | -53.34385 | 2025-08-08 05:01:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03c051c2-8db7-3977-9ab9-120a2b00ad03 | -12.52591 | -47.12504 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33bb6434-1e90-30d3-a876-1bf431a85e6c | -13.05593 | -56.84936 | 2025-08-08 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff48a6dc-41c7-3e1c-895b-8b68c967a876 | -11.19268 | -51.43425 | 2025-08-08 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21bdf192-1625-3cd6-aa62-1925f61edc3c | -9.71026 | -61.30095 | 2025-08-08 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 542d7b58-dd41-37f8-abcf-8248ad2b354e | -9.94363 | -60.50372 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8cd8c65-ef8c-3da0-8fc1-5c27020f6faa | -12.33874 | -46.05713 | 2025-08-08 05:01:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 739a70d2-dafd-3597-95fe-d0da70218482 | -11.19201 | -51.43876 | 2025-08-08 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3723eb8d-0a7f-31fd-a23b-a417cbf60352 | -9.64671 | -62.91039 | 2025-08-08 05:01:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80f4c5db-d8b8-3bed-b6c9-15e757bc27af | -13.05475 | -56.85665 | 2025-08-08 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d5e3b85-43e3-33b2-94a1-1da3233d2ad2 | -12.58511 | -47.17686 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 66d07738-98cd-34f2-8e40-5c52d93cfa1f | -9.64487 | -62.91463 | 2025-08-08 05:01:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8d18441-3b31-3ea1-8e6a-daacaf1bebb6 | -12.09529 | -44.73806 | 2025-08-08 05:01:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a33fb52-27f9-3a40-b5f0-7cdd33a9bb98 | -12.72125 | -46.37313 | 2025-08-08 05:01:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8275599c-f0cb-3bd8-bd03-8d77e37bb693 | -9.70661 | -61.30207 | 2025-08-08 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4fa7a0f0-ac60-3712-9ecf-5f4f4a93cc11 | -9.93575 | -60.47457 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1917f31-b0ab-3fc0-aeb4-9d596ce2e7a9 | -13.05416 | -56.86029 | 2025-08-08 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e44f01c-6c08-3778-af3d-04d2d113fd32 | -12.54394 | -47.13691 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| be82cd3d-0a8b-3170-83ef-28f9c6b5c466 | -9.93357 | -60.46232 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6b35c33-638c-3369-aea7-5b9cfd0b5808 | -12.52825 | -47.13923 | 2025-08-08 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 17eaaccc-0715-3cca-9ab5-d1db3ccff9d6 | -15.55203 | -43.26822 | 2025-08-08 05:01:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b43105b7-0c17-36ad-9768-afac2e0c6dc3 | -11.19963 | -51.44283 | 2025-08-08 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b366d29-68a2-3fb4-b894-dd3462a91eab | -11.74907 | -47.50664 | 2025-08-08 05:01:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| af62c51d-0526-3cab-886d-9360c08be32f | -9.93641 | -60.47073 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9be50a28-0934-3e96-8abb-cd44addc6e19 | -13.04625 | -56.86644 | 2025-08-08 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be807adf-4059-3cd3-900c-db2982b9646c | -9.92526 | -60.46076 | 2025-08-08 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d196fe4-10c7-3497-9526-5d741fab64cd | -9.70379 | -61.28633 | 2025-08-08 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d830495-a969-331e-b4f0-aca5d0fa8157 | -11.03727 | -55.37275 | 2025-08-08 05:01:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e76319f-e7ff-3731-b5f5-4932b9d70bd2 | -19.13185 | -43.51854 | 2025-08-08 05:01:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README22.md)

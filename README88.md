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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e096ef46-6013-3dab-ba90-89aa5d999882 | -3.38405 | -50.14157 | 2025-10-08 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8483ec87-9501-3594-9eab-e35f1a2ffd37 | -3.39002 | -50.14479 | 2025-10-08 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 311a5a25-842f-3b4b-ad57-57ae68931053 | -3.11356 | -48.78432 | 2025-10-08 05:27:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98045fed-97d5-339d-9e39-0b0d219340ea | -4.92171 | -48.54279 | 2025-10-08 05:27:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0fdd0b19-b680-3e89-948b-6ec316e6d61d | -3.08734 | -50.57362 | 2025-10-08 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a1e3a689-ed61-3767-aa3c-a92702167a36 | -2.89082 | -50.72979 | 2025-10-08 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a6998e5d-94ed-3d8b-af8a-847659a04952 | -3.78981 | -49.43396 | 2025-10-08 05:27:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7fb63879-a245-34ae-bb85-ddcc6925bb1e | -1.0946 | -53.68963 | 2025-10-08 05:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 100d399b-bbe0-36ee-962c-d1f33e554253 | -3.08606 | -50.58218 | 2025-10-08 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 891662c4-b46d-344f-892b-735e307e41b0 | -3.09048 | -50.57464 | 2025-10-08 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9d35e35-0e7d-3b42-83eb-2f5778bcc4fa | -1.87592 | -55.15954 | 2025-10-08 05:27:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 482b562e-10f6-3afd-a1a2-ba14b56a1c13 | -0.9092 | -47.54737 | 2025-10-08 05:27:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 522ae791-e471-3c89-919c-04f868c89ae7 | -3.08799 | -50.56927 | 2025-10-08 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9cca4e4-18f2-3e0f-b80f-35a6e6515387 | -2.88494 | -50.72884 | 2025-10-08 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 758029af-c6d3-30b4-8f1e-9e99ad45645a | 0.9233 | -51.12661 | 2025-10-08 05:27:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0947f775-e636-3ff2-af68-dee0ee1dd98e | -2.89144 | -50.72552 | 2025-10-08 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4338a2f-bb53-3753-a9ec-d575f32de597 | 0.92816 | -51.12223 | 2025-10-08 05:27:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fad8d8c6-b179-37dd-9fe2-da713d12e447 | -3.09265 | -50.57891 | 2025-10-08 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77141fb5-1d39-3d3c-8393-48d46453428a | -0.90229 | -47.54601 | 2025-10-08 05:27:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8ef84997-1759-3672-acdd-2f6f8a44c7d0 | -3.08926 | -51.24969 | 2025-10-08 05:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2cdc243-d5fa-3295-92b7-f08167ce0508 | -3.08393 | -50.57789 | 2025-10-08 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 320d15c6-ac4d-3904-8c51-5301dd641250 | -2.8902 | -50.73407 | 2025-10-08 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5a0864af-cd31-39a9-a788-0fdfd0d52e63 | -3.57606 | -49.43768 | 2025-10-08 05:27:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 959a27ae-9b16-34d0-bed2-e0eee71c5190 | -2.52229 | -51.93185 | 2025-10-08 05:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0b73fc40-3c1f-345d-ba4a-3965f42164ab | -1.09924 | -53.69068 | 2025-10-08 05:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c5e6cd1-4d97-3079-a173-2e6622bc56af | -3.09396 | -50.57016 | 2025-10-08 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db190e81-71e2-302f-b3b6-bd250a647e37 | -3.19907 | -51.01922 | 2025-10-08 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ecbe8b1-7a7f-3ceb-ae67-e164f4493385 | -3.08453 | -50.57362 | 2025-10-08 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c423bfab-efbc-3dd3-846d-8efcb71b750c | -3.09111 | -50.57025 | 2025-10-08 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 370f8950-254b-3553-a286-9b458e204517 | -3.14237 | -50.29712 | 2025-10-08 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d0b5865-6166-3711-bc53-39f9b7b940f4 | -1.75312 | -55.2479 | 2025-10-08 05:27:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27a1a474-2d6d-3b13-b640-cc1e3669d5f3 | -2.51689 | -51.93093 | 2025-10-08 05:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95557923-4505-336e-a593-e6e49a245020 | -2.5174 | -51.92754 | 2025-10-08 05:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 889bb38d-5cc0-3b59-b43b-df1e3489e105 | -3.1093 | -47.79535 | 2025-10-08 05:27:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| efccdf8a-003a-3bb7-9cec-977c200c7e8b | -3.08987 | -50.57898 | 2025-10-08 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ae12d348-cd54-35c5-8815-562aff6f16e8 | -3.0867 | -50.57793 | 2025-10-08 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 043065b3-6010-39d3-baba-2305b5afd668 | -3.78976 | -49.43107 | 2025-10-08 05:27:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| de4b80bd-741a-3c6c-9d03-c271875e762c | -3.12025 | -48.78514 | 2025-10-08 05:27:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b09dba5-58ee-3d86-a202-367f98498a74 | -11.72933 | -50.92568 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d10cb33-bd35-3fe6-8f2e-76ec9503ae0d | -12.39104 | -51.1444 | 2025-10-08 05:29:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 588bdb2b-7370-365f-85ef-26b33ce4eb63 | -11.18133 | -54.88323 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 69b4d32e-91d1-3ec2-9e67-58519414678f | -11.69875 | -50.96162 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f43d12c4-23fc-38ac-94fe-39a5478aac56 | -12.39232 | -51.13333 | 2025-10-08 05:29:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2c57227-b8b2-3c09-a842-34d2be0a673a | -11.16676 | -54.87975 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ac766fae-93c2-3f46-8410-e66ef2a5e426 | -6.59815 | -59.11269 | 2025-10-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4317f51c-06b4-3963-8fd0-4e528a7b0a67 | -11.01365 | -50.89072 | 2025-10-08 05:29:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98e7e0f1-1127-34d0-8474-d873284881d4 | -10.24316 | -52.69807 | 2025-10-08 05:29:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c136209b-8b3e-3b86-9415-2c274f36f502 | -10.46748 | -52.16725 | 2025-10-08 05:29:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9d9e56d1-0c13-367e-9d35-523c9c3d194e | -11.17836 | -54.86935 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5da118fe-a857-3680-9b86-900893887591 | -6.46026 | -62.83661 | 2025-10-08 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 875384e0-5df6-3108-9b99-61e8252b600f | -11.17127 | -54.88194 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cc6e28d6-a1ca-323b-aa46-08c5bce272c2 | -7.58662 | -64.51129 | 2025-10-08 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 829e48ba-1b63-3851-a61b-49678647b059 | -11.72483 | -50.965 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 805033cb-7486-3564-9507-0f6e94445f44 | -10.64601 | -58.76501 | 2025-10-08 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bf06091-071c-3bda-87ae-892abe6b10df | -11.14169 | -54.87586 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 08e0cdf5-ba7b-3f5a-95a6-ef7aa38a6f5c | -11.13939 | -54.89367 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d914fa1-e0df-37bf-83a1-8bda559725a7 | -11.33679 | -56.2013 | 2025-10-08 05:29:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5f8ff365-326d-3a45-9162-e619f15fec25 | -10.36388 | -58.51644 | 2025-10-08 05:29:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3d8c246-5a55-3895-93a8-a969708043c9 | -11.75594 | -50.92162 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 979bf8e7-1735-3855-86c7-f50eaac8179d | -11.16561 | -54.88852 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90fcf0d4-fb5c-3257-9588-18a71340ecdc | -11.15673 | -54.87819 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c30b31c6-a19a-3d6a-9531-63086a7d86fb | -11.75154 | -50.90562 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 22.7 |
| e6985a74-744d-31c2-9b25-d7f28314adc5 | -11.15133 | -54.88041 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef5bcd5c-2cf4-3acc-b21b-2a03d10439dd | -11.72215 | -50.93046 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09f25499-ced0-35f4-8f83-bc3e23e769e4 | -11.1413 | -54.87889 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac6aadd5-4c28-3149-aa6c-6704a5070c06 | -9.19871 | -59.591 | 2025-10-08 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d82aa91-9cde-33c3-87d8-5b45ae0a200f | -11.74763 | -50.93946 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 23.9 |
| c63afd96-37fa-38ea-8c00-dc12d08656eb | -11.33188 | -56.20417 | 2025-10-08 05:29:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dcacf2e7-b75c-335d-904e-c561407ae57e | -11.74817 | -50.93204 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| b6888cdf-5c4a-3cb8-9274-c1ebaadc844e | -10.04396 | -59.3614 | 2025-10-08 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1f07dae-d9e4-3f6f-abf6-037657722e60 | -11.14631 | -54.87968 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37b245a7-b97b-322d-ae08-d82da0f7b8d3 | -11.73651 | -50.92089 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 17f54cc7-a161-3622-8d93-7274ef8849f0 | -6.94884 | -63.10348 | 2025-10-08 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bbd1aa40-cbb8-3abb-9377-722cc719bbcc | -11.11399 | -54.04345 | 2025-10-08 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 597af5e9-4355-39ee-8a6f-dfed545613f9 | -10.89322 | -51.02432 | 2025-10-08 05:29:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b07ecb45-d03d-3020-bedb-5a8cbe2d063a | -11.73449 | -50.93594 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8ce47946-b124-3dad-91eb-dcef594a0da8 | -11.70002 | -50.95041 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bc7b378e-35a8-32d0-81ff-3fa5994181f8 | -6.8204 | -63.07609 | 2025-10-08 05:29:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4c964cd-154e-38c2-b700-dc8a6cfd1b47 | -11.15327 | -54.86547 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47267315-4709-3dee-8d55-51e2211d2588 | -6.45695 | -62.83609 | 2025-10-08 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 580bda7d-bb04-3a70-ae06-f367e9e1b993 | -11.1731 | -54.86707 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 198ad873-6522-3430-8f97-5c3eedd62c7a | -10.99936 | -50.90008 | 2025-10-08 05:29:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3745e79c-51f8-3b5b-ac0d-fcf8da21eae9 | -7.59408 | -64.50864 | 2025-10-08 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 456c2b2f-635b-3249-909d-2fe2a3633c7c | -11.17487 | -54.89415 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fa04a876-02de-3eb1-be33-0764bcc4ae95 | -7.47064 | -63.56968 | 2025-10-08 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2df5805a-0e8c-3d44-91c6-849aed09a2f5 | -12.3917 | -51.14071 | 2025-10-08 05:29:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bf6d5198-c9d3-3af3-809a-ab405af2a0de | -11.1807 | -54.89045 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 0198afba-f180-3bbb-9b1e-846853e1bd03 | -11.73693 | -50.91339 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 82664eba-e238-3e44-8acc-edcb228b86ee | -11.17091 | -54.88486 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| a9623664-ec53-39cf-8032-594f60e51f23 | -11.15018 | -54.88924 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4f098bfc-53f0-3e26-8c28-0e0be95770dc | -6.69061 | -58.81339 | 2025-10-08 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8426c40a-4851-3fee-8d44-3863dabcc346 | -11.14014 | -54.88784 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f361ca1-d6fa-37ea-b0ea-fc765b273673 | -11.17101 | -54.88633 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2500ea7f-0d66-3b86-9f86-523164a98c77 | -9.16995 | -59.56089 | 2025-10-08 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f3a3237-cebf-36ee-98e1-0c56df158a20 | -10.36335 | -50.2875 | 2025-10-08 05:29:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d99f3341-1483-3278-bc89-eacbbc85d4f4 | -11.17881 | -54.90348 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4678bac-847f-369a-96e4-8bff26bb8b95 | -11.15211 | -54.87443 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0efd4c4-f30a-3161-9f06-4a7bf9f65b14 | -12.39168 | -51.13888 | 2025-10-08 05:29:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47e032b6-a50b-3531-9455-f400c347aa65 | -9.38439 | -59.42494 | 2025-10-08 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f8bf199-4ad9-3c75-bb3c-2bb8ca7c3656 | -11.17666 | -54.87968 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |


[Clique aqui para ver as próximas entradas](README89.md)

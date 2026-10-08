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

## Dados Diários - Página 145

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db60242b-6119-30ca-956a-4a6e0cdc0e6f | -3.35151 | -50.47631 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 980763b7-2b4e-3864-b262-6e2bf133a763 | -1.61539 | -55.1146 | 2026-10-08 05:23:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b553d25-9341-39d9-974f-ba2c1709a619 | -2.50038 | -56.23076 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf6c91ca-9850-3512-8a6c-956c51b14b04 | -3.59733 | -54.56458 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 798a428d-448c-36fa-aab7-ccd7b94a5e0f | -3.70863 | -59.6728 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63b93cdd-ab37-3cba-9f9b-b9bd735f347e | -2.82222 | -54.10292 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71522c85-4b84-3157-af7e-0916afc42e1e | -3.60366 | -54.56944 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 03357d1e-35a9-3277-b491-f89d65110926 | -3.55927 | -59.47046 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4b8c18a3-8274-3f05-a280-a414d823dfaa | -3.27764 | -50.03579 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2694edfd-58d9-3fa5-9359-1fed1c19e535 | -4.06265 | -59.83923 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| df76fafa-d6f4-3f0e-8fc8-c208ef0f10bf | -3.04571 | -54.14827 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e6689cf1-00bf-3f41-aa75-5d82d76f5438 | -3.38209 | -58.23795 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 226cc080-179e-33d6-a91a-1915c259dcdf | -3.14216 | -53.71998 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1dcec5c0-b801-3865-b6e1-7ecdb302cb36 | -4.06052 | -55.32708 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80af90bd-9a22-3213-abb6-b6c7362e3843 | -1.40253 | -54.61 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8538ed32-d0a8-32f5-a7e3-ed1cd69c0195 | -2.56635 | -56.17366 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 754acf00-6a3f-3c11-8a0e-8ffc05b4aa63 | -3.65527 | -60.63241 | 2026-10-08 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3a34800f-a123-32dc-8029-f13f63683084 | -3.56406 | -54.22019 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc1e6931-4381-32ca-81a2-a37d688bfd41 | -2.64669 | -56.54437 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86f3e7ce-7eba-327d-b830-3da53604f002 | -3.18588 | -50.5598 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7ef5381-3a9e-3755-9225-2bf39f93532e | 0.44852 | -60.53981 | 2026-10-08 05:23:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 26bdaac5-47fa-31a4-ab1f-310792a88843 | -3.61241 | -55.46708 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60439ebf-1db9-30ad-8371-cc40d2353885 | -4.91993 | -55.85855 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 032a7068-c016-3868-ad86-bbecb7adc4f3 | -8.60052 | -47.14682 | 2026-10-08 05:23:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac5f189e-525a-35a7-a150-4526d93aac36 | -6.6849 | -55.09644 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95d70f92-a4b7-35d3-8088-19689a78de07 | -3.8815 | -55.79867 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 389671c4-0f42-3317-b656-6cdc91deb52c | -3.8406 | -55.41495 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fd83e012-902c-345d-aa7f-61e45df67915 | -3.86296 | -50.4137 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 10ad3706-b7df-39be-bae7-33e40033170c | -4.56987 | -54.95225 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 622d5860-dd8c-33d5-881f-062b2c9dfdf1 | -8.59739 | -67.30108 | 2026-10-08 05:23:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0bb29828-7dfd-3a99-8d3a-e9d65fabf252 | -3.19275 | -50.5441 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7efe2410-e843-37b5-a60c-b894daa1246f | -4.34987 | -55.13013 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 320d334f-70f9-3c45-986e-011cfc81cbe8 | -3.06655 | -54.17516 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3919dc0a-a7f6-3041-a404-38b86e803c40 | -4.54177 | -59.92285 | 2026-10-08 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edb6b830-873a-3ee6-a9d2-ed531d7bd42d | 0.9117 | -59.62831 | 2026-10-08 05:23:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b376982-20b3-3c11-9187-1ed5521f91d4 | -3.69391 | -59.6494 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6a8e4c09-57e3-3ac9-b9f2-5e07d9c27aa0 | -3.16431 | -58.63648 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 899af35d-e353-3cb5-a1f2-f19e135aa5b7 | -4.56527 | -54.95912 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e12c6b10-45be-3502-8be2-7a6cfa084a00 | -4.09314 | -54.62271 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0759f332-35f9-3db4-afeb-40d208a57e79 | -3.96687 | -55.83342 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8bfa159-cb82-38aa-adf8-a51096c89c78 | -4.92273 | -55.86263 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f038f6c3-8070-31ab-9d53-861a92e9e6c2 | -3.09788 | -53.746 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0c6df68-3a86-3d56-bd34-521763b08c7e | -3.56641 | -59.47161 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4957be52-c3b8-3446-80ac-857bf0edc6d0 | -3.86739 | -50.41428 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 686759f3-1a9e-33e2-965c-985581139312 | -3.09093 | -53.72029 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59ce69e6-7c0f-38bb-b7a3-fd2dd67f7e5a | -3.28199 | -54.0438 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea2725b1-0423-3c42-a6c9-6d3172945368 | -3.69031 | -59.64882 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee3edb16-6808-3cb7-84aa-29c281dac91b | -3.55686 | -54.66578 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16292bda-9005-3b89-abbf-43b8b575d4f4 | -3.43661 | -56.93793 | 2026-10-08 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97a067e2-46d7-3bb5-9c22-34708787f930 | -3.31245 | -54.05653 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ef26a533-c067-377c-ba80-55ad217e3f30 | -5.69411 | -53.49778 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 858e99d7-14a7-3dc5-bac6-42ea43022fd2 | -3.02104 | -54.05327 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| de9aa666-f059-3321-aee3-948061306823 | -2.84368 | -54.12594 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f11b90cb-7881-3e13-8ab7-073819312c71 | -2.78364 | -56.49132 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e153d143-3584-3ba0-83e2-f62b3e3df41c | -1.60809 | -55.16048 | 2026-10-08 05:23:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a7aecbe-1ca7-3558-956f-c866de026e42 | -3.22189 | -53.96699 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad30b7d0-6d65-3ee9-9f3c-59109e47a48a | -2.49287 | -56.0631 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea61d548-bb06-3ce5-92d2-ab0dbbbf3a21 | -3.44574 | -59.82447 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f11c7e1f-c07a-3d82-a813-788fac64f38e | -2.85246 | -59.11441 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5d6f8b33-78b8-3811-942a-575764e19742 | -2.88101 | -54.11893 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 320d4ae9-8407-389f-9db5-1499843575ec | -3.29468 | -54.07772 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 894bf471-d3cb-36cd-b37b-ef893e549261 | -4.1557 | -55.14514 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b453be21-c098-355d-9618-647468a1da22 | -3.22948 | -57.88033 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5ce7a65d-d018-3991-acac-8e71ea9d3814 | -2.15382 | -51.97658 | 2026-10-08 05:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be6387cb-75fd-36f0-baed-d5a07f07943f | -3.00381 | -57.74258 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1aa3d4ee-de36-39c8-a4be-aa402c625229 | -4.56928 | -54.95598 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| de9a86be-ef92-3f05-b94f-950891c2e22f | -3.01101 | -54.07161 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5e240da4-4e99-3d27-b2a1-a8b8b7b90280 | -6.72804 | -55.12596 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 14bf5f48-bef6-3c23-b8ea-09a885493ab0 | -3.53417 | -59.47958 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69350408-d747-33af-9d1d-4a0f0020eb95 | -3.28276 | -54.01583 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bc79a34-d57d-35e3-94f5-981fbef1fdb2 | -6.88503 | -43.68924 | 2026-10-08 05:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7ad4ffa9-b391-34fd-bffa-47a989438511 | -3.11675 | -54.17785 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8fb51b38-f288-33ab-8716-98735a31e0a5 | -2.46738 | -56.07328 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ed3ebef6-1999-37cf-a003-bc8dd85f0d8e | -3.04521 | -53.92085 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09e2fde7-97e3-3401-b9c8-6b122ef161f3 | -3.18552 | -58.65921 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84fa6c86-b0b0-37f8-b890-fb62e752821b | -3.65981 | -60.62843 | 2026-10-08 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93f352fc-13ae-3d87-9447-df297a6bc575 | -3.28797 | -54.02867 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbefcfa9-dac5-384b-8a73-8be486e52973 | -2.46498 | -58.01302 | 2026-10-08 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21cabee1-b90f-3f73-b999-bdcb5a15cd1f | -3.47131 | -59.57362 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9fc5c492-6045-3f8d-a103-000b3862c4dc | -3.57154 | -54.35521 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ae036ae-cec2-381b-9470-c57fa290c150 | -2.39731 | -57.89058 | 2026-10-08 05:23:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b8519e2-5062-3329-bdd2-cff3ec417044 | -3.59616 | -54.57209 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9792db97-20bb-315c-a3ba-b2e9e2929807 | -3.02093 | -54.07713 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0f687967-c689-314b-a89b-34b1b417fb36 | -2.99322 | -54.1401 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1df5f34b-95cc-38d3-859b-161d37fdec54 | -3.01322 | -54.10366 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 2a832208-0f4f-32ab-8d85-003ff3946e51 | -2.78532 | -56.50219 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aedb5bc2-3636-36ed-9cf7-e7a39b364a74 | -1.47854 | -53.61446 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58a31f6b-cfaf-3941-ac4d-052c76465cdc | -3.15955 | -50.44179 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38ebf01a-d786-3e18-87c9-506f12bb97cd | -5.22826 | -60.24027 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4042259f-fafe-30a1-b0ab-f2a0b77aed15 | -3.02977 | -54.06658 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4808374c-caaf-37ce-ad50-5e926c7fb622 | -2.22269 | -58.11004 | 2026-10-08 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2966858-d172-3b59-8e04-fa4a86e26e10 | -3.59153 | -54.57911 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d7c0b3ee-caf8-359a-bb93-ebbedc05ad94 | -3.57872 | -61.62578 | 2026-10-08 05:23:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24415d54-518a-3d54-b44c-e8981f8c5134 | -4.53545 | -55.61686 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c9d5db0-4000-313a-a5b3-0c78acca2d81 | -3.08098 | -54.24707 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 983fe275-0a6c-3eac-86ae-f092995ebb37 | -4.26867 | -54.87238 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d32055e5-01bf-31dd-9a54-4ee13f11d2b8 | -4.12361 | -59.87715 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6e51a4b1-2821-3505-8d91-a5d4ff0ed87d | -4.57617 | -54.95698 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7236d939-d3d2-319b-8332-7b4cdc170c7b | -3.09944 | -54.28905 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87c4c86e-9b63-30b9-8fc9-9f95b9d261b5 | -2.49185 | -56.11256 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README146.md)

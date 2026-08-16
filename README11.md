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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ccfeb6a-b350-345d-a855-df172bb15334 | -14.28822 | -51.95135 | 2026-08-16 03:55:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| de7a9977-3e8d-342d-9da5-21e5f07561fb | -12.67414 | -48.45277 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11a83157-e639-3e5b-b119-64fca2df7cb5 | -13.49746 | -48.23715 | 2026-08-16 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78340f2f-bf36-36b6-8b45-e9170dd1cf8a | -15.14139 | -48.12407 | 2026-08-16 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dfe5a930-4441-3a80-b1a0-0f97da367478 | -12.0166 | -46.4352 | 2026-08-16 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 6bf36de9-0c53-3819-8614-28ead76ba4fb | -15.17061 | -50.07282 | 2026-08-16 03:55:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd972f37-8a83-3e56-9405-0e97ee7f05e6 | -14.97886 | -46.58463 | 2026-08-16 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8ae9c96-d42a-3fab-b57a-21bdfebc58cf | -12.64359 | -43.90168 | 2026-08-16 03:55:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ea0e245-ae68-3bbc-b40f-50c03112d414 | -14.90398 | -46.63752 | 2026-08-16 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 24960573-65a7-369c-86fc-5747b80459ab | -14.41229 | -51.94035 | 2026-08-16 03:55:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f736001e-de2b-3acb-9551-310a9074ca4a | -13.49336 | -48.22951 | 2026-08-16 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 944010b8-90fc-3c25-913a-9db3a0f86b98 | -11.45289 | -46.60818 | 2026-08-16 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64423f4a-057e-3910-a9d4-8d45e725937c | -14.90275 | -46.64396 | 2026-08-16 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 610e6c74-4324-3847-9885-7e68347a2b8e | -10.53846 | -44.87222 | 2026-08-16 03:55:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ba91a642-f5e7-3d76-a78f-8ea29605adba | -12.03296 | -46.43624 | 2026-08-16 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 40a6c735-e3c9-3759-ba67-d309b59cc15c | -14.42445 | -51.83396 | 2026-08-16 03:55:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c0ad82e-84ba-3ffc-8c3a-e2dbe7e80aad | -15.04694 | -47.02465 | 2026-08-16 03:55:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8adbcc41-ee01-3cab-9304-86187e6f1370 | -11.91496 | -49.33166 | 2026-08-16 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52644ee3-4f53-3d1e-ba5b-73d7b6d5b69e | -10.26029 | -46.30674 | 2026-08-16 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46322c04-113a-34b1-b415-ba659b8b5cd5 | -14.93812 | -46.6129 | 2026-08-16 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a22dfa7d-4b5e-3448-bc63-d4855e77f301 | -12.67896 | -48.45757 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef755a27-5539-3761-a624-ee3296ab5cad | -10.45767 | -46.29881 | 2026-08-16 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af238d7c-cc0d-34d2-8f8b-a290c424b674 | -12.68688 | -48.47591 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ccf55a22-42a7-31b9-8a49-37e2a9678a8a | -12.01553 | -46.44097 | 2026-08-16 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 7dc7c225-1c38-3052-a0c4-bed5e8f78d0a | -10.15745 | -48.08472 | 2026-08-16 03:55:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78ff7c0a-bf5a-3ee5-b193-0bea448304ec | -12.74643 | -48.43642 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 748440b7-c75e-38a9-879c-adb439de4729 | -11.47562 | -46.59787 | 2026-08-16 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f0e1803-b738-3068-a238-8a0177e17fd6 | -12.68359 | -48.4633 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c606db6f-4149-3be5-a761-9f19aac47105 | -11.90814 | -49.3348 | 2026-08-16 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 695d47cb-b1e5-396d-8268-c3e0503f182e | -11.33618 | -46.21365 | 2026-08-16 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 75426181-9b16-3a4a-8e53-84783ab14c7e | -11.57611 | -46.79913 | 2026-08-16 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd393e51-51a6-3f2d-9014-82562d476c15 | -11.35858 | -46.28409 | 2026-08-16 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aaedecab-e4ae-3a04-aec9-968d10ee65b3 | -12.71091 | -48.47104 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 87eca5b2-5c5a-3c00-9d4e-9925071df4c2 | -12.64838 | -43.8987 | 2026-08-16 03:55:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51209818-a9d7-3ba2-a789-eee074778f10 | -12.71163 | -48.4674 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 537bc690-db76-3921-a2c7-e33accb61364 | -11.32505 | -46.21865 | 2026-08-16 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67d24d83-920f-30d7-9988-e8ecd8e3f57a | -11.62046 | -51.09008 | 2026-08-16 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5bd1b5b9-eb94-32dd-9456-60a074b6d688 | -11.91182 | -49.33342 | 2026-08-16 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 99220504-c086-39a0-9fb5-30de74f6513a | -11.46613 | -46.59288 | 2026-08-16 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be7b5c35-449d-3613-a005-e372cdac68d1 | -13.56195 | -49.06014 | 2026-08-16 03:55:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06f43aff-0bde-3fe5-8d9a-ef9dbe746bce | -15.53973 | -47.39036 | 2026-08-16 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bcd665fd-b43b-3004-b20c-ef4d58863deb | -11.90398 | -45.97649 | 2026-08-16 03:55:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e619cc50-5aa4-3dec-ad2a-1b0d75709c02 | -12.23108 | -43.14465 | 2026-08-16 03:55:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8c55e5ff-3d6d-3831-91c7-065a405d0f68 | -12.70286 | -48.48272 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 340a2f02-16e8-3be3-9c89-dafa0541bb29 | -11.4611 | -46.61482 | 2026-08-16 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9cf258b8-ab5c-388b-a29e-58bce9f7ddd5 | -14.41236 | -51.95564 | 2026-08-16 03:55:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2352f5a0-d688-342f-8097-057224095c53 | -12.27894 | -45.89989 | 2026-08-16 03:55:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 52973b09-6a28-3b7d-9744-d4330694b061 | -12.70528 | -48.47038 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fc862a1e-9c51-30f1-8900-d4bc51dea43c | -9.10831 | -46.38536 | 2026-08-16 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 576df601-ff29-3510-91fa-9a6e8e160e23 | -9.10776 | -46.38839 | 2026-08-16 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1a7a538-c073-3001-9bff-20e9bf3735e4 | -14.41492 | -51.94359 | 2026-08-16 03:55:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db365755-dc5c-33a2-9a4a-3c8b340d4a8f | -9.09637 | -46.3923 | 2026-08-16 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1018bb2b-21e4-3513-b496-6c4a660bfe76 | -12.03588 | -46.44112 | 2026-08-16 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| d38a582d-9965-3a61-8496-e73c9afa800c | -13.4981 | -48.2339 | 2026-08-16 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd0554b3-0bb0-3b53-a053-5a93efdb699a | -14.28954 | -51.9454 | 2026-08-16 03:55:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa537fc7-e612-3c5f-a924-0bf8b8d8c67c | -13.54595 | -46.24831 | 2026-08-16 03:55:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4022283e-0e86-399b-8d0e-aa5d374bdb4b | -15.14875 | -48.62726 | 2026-08-16 03:55:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e876aa24-3f95-3db9-b492-64ce3ae32d94 | -15.06879 | -47.0318 | 2026-08-16 03:55:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d25e1ea-f355-3aa1-8816-48354cb4f53c | -15.06279 | -47.03659 | 2026-08-16 03:55:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47fcf7c1-d8ad-3ccf-931b-cad0056061db | -14.29112 | -47.19022 | 2026-08-16 03:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3238c98e-e4b3-306a-9dfa-3328b2366995 | -14.41665 | -51.83825 | 2026-08-16 03:55:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b67337b6-da03-3f83-b214-bd0bbd59f661 | -15.18095 | -49.50252 | 2026-08-16 03:55:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 865b8546-b148-31ca-acdd-e68524551697 | -13.48733 | -48.23169 | 2026-08-16 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abb77b52-ddf3-33bd-b13d-1d3d81109b20 | -13.50347 | -48.23507 | 2026-08-16 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7eea3b94-9e9b-370c-a35a-f21eb81243f4 | -14.48855 | -45.689 | 2026-08-16 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5fcf797b-c9be-32cb-98da-b772bb6493a7 | -12.46949 | -46.66419 | 2026-08-16 03:55:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66fa0bf4-029c-3187-aae3-892ebc416eb2 | -15.08836 | -48.70364 | 2026-08-16 03:55:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 839b06e5-ec13-3c5a-aedb-ac742781eaa6 | -12.6874 | -48.444 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd551b19-59f5-3220-9a86-f41b8327972f | -11.31374 | -47.01034 | 2026-08-16 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29a1172b-d98a-3f81-be1d-c4983604f481 | -9.60229 | -46.04528 | 2026-08-16 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c8823f4-3771-3eee-8e67-c9fa5f435e0c | -13.69408 | -46.24578 | 2026-08-16 03:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0c5fc0c6-f0d9-36f3-9b51-3c769c0b8fc8 | -15.14389 | -48.62369 | 2026-08-16 03:55:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 24c8e586-4502-3e9e-a2c4-fd0d7d62f062 | -14.91718 | -46.61985 | 2026-08-16 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bd7f27b9-6bda-35e4-807c-88e52c46d5e1 | -11.8837 | -50.62522 | 2026-08-16 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 09db9bf9-1e60-3a7c-983c-8fb54d22e43e | -13.68745 | -46.25511 | 2026-08-16 03:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c5c1506-e182-3f47-868f-38a38b26c04a | -12.44565 | -46.65218 | 2026-08-16 03:55:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c8b713ca-16c9-32d3-a2f7-a906804abc4e | -12.03689 | -46.4423 | 2026-08-16 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a7922e38-9d25-39ce-977e-f5e135611cde | -13.48798 | -48.22839 | 2026-08-16 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99abe699-7a5e-333e-9511-113f4ef408b8 | -15.10241 | -48.71742 | 2026-08-16 03:55:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a5c0f9b-3925-3461-bf15-c19f3d64827c | -14.92288 | -46.61565 | 2026-08-16 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a14a9b41-e685-3dbe-94b9-7366b650e50f | -10.52283 | -44.85469 | 2026-08-16 03:55:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5db3873d-9607-3365-b027-2b6825a23fa3 | -13.43896 | -43.85498 | 2026-08-16 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84fde63d-4053-33b1-aab7-97d958bbf0d1 | -11.88394 | -50.62624 | 2026-08-16 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bdb41823-bc26-396d-935f-7eafcc5d94a7 | -11.31434 | -47.00723 | 2026-08-16 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 046e961c-a91d-3b8c-a390-cc6652716126 | -15.06639 | -47.01855 | 2026-08-16 03:55:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 38658b4b-5515-316d-af9e-ba091370bff4 | -10.67655 | -49.00257 | 2026-08-16 03:55:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7eb2651a-005c-33d4-a965-aa1588e792f5 | -11.43144 | -43.91525 | 2026-08-16 03:55:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39ba44fd-25df-3d92-8b92-24720ac2f449 | -11.79661 | -51.79377 | 2026-08-16 03:55:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b00cb22a-8d91-36bc-95a4-9eef3a1f87fd | -11.46059 | -46.59471 | 2026-08-16 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1bbe0da-6f9f-3167-ab88-34a27b8d9155 | -11.45348 | -46.60496 | 2026-08-16 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8bc13cab-681c-336d-ab0d-9fba533f8fbd | -15.0583 | -42.48878 | 2026-08-16 03:55:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2d3e374c-a342-33ef-bf14-c27ca6c01788 | -14.92768 | -46.6162 | 2026-08-16 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 493fe9dc-0d1a-34bc-9c1e-d4595b372542 | -11.80865 | -44.80755 | 2026-08-16 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37ab953e-f752-3360-a4cc-e54e17a7aa0f | -15.08908 | -48.70012 | 2026-08-16 03:55:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9745609c-f5ca-300c-88aa-ccfc39b62afc | -13.68271 | -46.25427 | 2026-08-16 03:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a374f947-fbfb-3e72-bf57-77de15ad5493 | -12.69311 | -48.44426 | 2026-08-16 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bc09854e-0ae9-3451-9565-c633de34b819 | -13.43962 | -43.8513 | 2026-08-16 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d72b4686-dce8-3521-bf28-0c520f50065e | -15.05786 | -47.02015 | 2026-08-16 03:55:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6a674c05-9f9d-3b22-b1d0-1cbbd39e121d | -14.28616 | -47.1892 | 2026-08-16 03:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d4ac45d-9e01-3997-82b0-dbf08eb213da | -14.41365 | -51.94958 | 2026-08-16 03:55:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README12.md)

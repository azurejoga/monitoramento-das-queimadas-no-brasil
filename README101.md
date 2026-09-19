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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf8d962a-01dc-3d16-a04b-a5ec606f4919 | -10.6928 | -60.7322 | 2026-09-19 08:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 3398f595-fab6-3221-9de1-0bc67e67b1c0 | -10.6928 | -60.7322 | 2026-09-19 08:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 775bcd4b-e284-33f3-a3cb-03adfa20fdfd | -10.7115 | -60.7312 | 2026-09-19 08:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| dc00f4d0-5dd0-3159-8028-b8e84d584907 | -10.7115 | -60.7312 | 2026-09-19 08:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 4a7e6a89-321c-3764-952b-1d7545e3592d | -10.7115 | -60.7312 | 2026-09-19 09:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 373f1276-86f8-3eaa-9a53-8bf702e8a995 | -11.7629 | -49.8391 | 2026-09-19 10:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 320c8eb0-1a01-3e73-b52b-c058e4589dc6 | -12.5952 | -49.1046 | 2026-09-19 10:50:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| f887594c-6d75-3ee8-9abf-52b33acf6aa9 | -11.782 | -49.8368 | 2026-09-19 10:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 4d9c16c6-f86f-3978-9f38-3b051e776da5 | -11.7823 | -49.8152 | 2026-09-19 10:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 134.5 |
| a9f24dd1-5ec0-34e8-8330-74e9f478f58d | -11.7823 | -49.8152 | 2026-09-19 11:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 11350d78-09a8-31c4-9e0a-3c12ddc98d14 | -9.2603 | -45.939 | 2026-09-19 11:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 302c5b86-8f9d-37be-88ee-6a9600d40e6e | -12.5952 | -49.1046 | 2026-09-19 11:00:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 60ac6129-d721-3c60-9607-1c1184794b94 | -11.7823 | -49.8152 | 2026-09-19 11:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 229.5 |
| 8781355a-c1b6-3153-a6fe-5d4292785b9c | -7.8565 | -45.1336 | 2026-09-19 11:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 095d1250-d8af-3129-bef5-375fff68de62 | -12.5952 | -49.1046 | 2026-09-19 11:10:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 164.3 |
| 7e8caf65-a251-3b72-952e-8b6f5cb9d719 | -7.8754 | -45.1318 | 2026-09-19 11:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 99.0 |
| da5f6625-a5a2-3636-95b4-8d5c9dbd15db | -9.2414 | -45.9411 | 2026-09-19 11:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 149.1 |
| 55ef6441-1082-3716-a058-ebee05bb9b67 | -12.5761 | -49.1071 | 2026-09-19 11:10:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 19e8c46a-dd93-34eb-a210-a32f91020fd8 | -9.2603 | -45.939 | 2026-09-19 11:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 693f656e-a683-3c98-81cf-757aa9eff024 | -7.8754 | -45.1318 | 2026-09-19 11:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 101.2 |
| e7f83b47-ae18-3d21-9393-bb9e181082fd | -11.9109 | -50.1232 | 2026-09-19 11:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| bea28441-6a2e-390c-b428-151a125d142b | -7.8565 | -45.1336 | 2026-09-19 11:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 88.2 |
| fff5eb1a-977a-38f7-8db8-ff06c8b455aa | -11.7823 | -49.8152 | 2026-09-19 11:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 194.8 |
| 911ff072-6c8c-373c-a1d1-3ee62cfd4bea | -12.5952 | -49.1046 | 2026-09-19 11:20:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 159.7 |
| fbd6684a-7147-3737-80f9-4f3fd008a9d7 | -11.1228 | -49.4384 | 2026-09-19 11:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 288c3e42-9f38-3405-af96-86876546aed1 | -10.567 | -51.3137 | 2026-09-19 11:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| d6c2b657-bcac-3863-a099-bec4780526a0 | -3.56903 | -43.49177 | 2026-09-19 11:25:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| ebf2eb8b-2a80-35cd-8a80-8310694b5508 | -5.73131 | -43.27727 | 2026-09-19 11:25:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f8e06a8d-0a62-3d01-8d62-a579e1fa433e | -5.49951 | -38.73605 | 2026-09-19 11:25:00 | TERRA_M-M | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 7b424532-9ed6-3582-b006-3f5d50248bac | -5.66095 | -43.38661 | 2026-09-19 11:25:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 58ca7d9b-e57e-31d1-81f4-6ddb102e0a6a | -3.57038 | -43.48241 | 2026-09-19 11:25:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 40d379e1-7557-32b8-b51c-4d0c3fa790c6 | -5.5301 | -43.83888 | 2026-09-19 11:25:00 | TERRA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d1b3ec4b-7511-3d24-bbfc-ac697a6189b0 | -5.73453 | -43.51435 | 2026-09-19 11:25:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9cb29f9c-fec7-339a-b223-ea4eca5377d3 | -4.56448 | -42.98705 | 2026-09-19 11:25:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 93b58d90-4e32-3af4-bd33-5233a82f7ce1 | -4.5556 | -42.9858 | 2026-09-19 11:25:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 4bb4b8dd-2a46-35d2-92eb-4677f77ed93e | -5.56938 | -43.50634 | 2026-09-19 11:25:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 580d351b-7aa3-3364-8e90-689f90520ce1 | -6.26576 | -41.66383 | 2026-09-19 11:25:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| f043d39b-7b0a-39d6-b317-27817841b2d1 | -5.80508 | -43.7263 | 2026-09-19 11:25:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e4d96ad0-d379-366a-afe9-b6d80626c4e5 | -5.61989 | -45.2444 | 2026-09-19 11:25:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8b84778f-ac6f-3f6a-a521-834bf458e827 | -5.73002 | -43.28622 | 2026-09-19 11:25:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 83a59e81-ab7f-346c-bf2a-d75e6004e6ba | -5.95055 | -38.10829 | 2026-09-19 11:25:00 | TERRA_M-M | TABOLEIRO GRANDE | RIO GRANDE DO NORTE | Brasil | 2413805 | 24 | 33 | nan | nan | nan | Caatinga | 32.8 |
| 54bf829a-174f-35aa-b68a-45846d057c96 | -5.6507 | -43.19582 | 2026-09-19 11:25:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 649945df-7fb8-3f67-abea-b6b24b58c330 | -3.1034 | -40.22912 | 2026-09-19 11:25:00 | TERRA_M-M | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 56.2 |
| af77b601-bd91-3a2c-aa72-6a69f8866704 | -5.51883 | -43.78968 | 2026-09-19 11:25:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 4e5e1069-2bef-3299-88cc-58c85852fbd8 | -2.91924 | -43.51986 | 2026-09-19 11:25:00 | TERRA_M-M | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 1f3504a6-c458-3ee2-971a-3d5a36244626 | -5.38007 | -42.84003 | 2026-09-19 11:25:00 | TERRA_M-M | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| ca963d39-92e3-316e-bd37-ce8675eb4a3f | -4.56577 | -42.97812 | 2026-09-19 11:25:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| fe5d522b-3287-3d0e-97bc-034977f881bc | -5.93997 | -42.08722 | 2026-09-19 11:25:00 | TERRA_M-M | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| f66aaf48-7ebf-38c5-b568-ee9841b8dce8 | -5.66227 | -43.37758 | 2026-09-19 11:25:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f5259073-d4b5-3919-a33b-c8cddfd9f613 | -4.30786 | -39.80037 | 2026-09-19 11:25:00 | TERRA_M-M | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| d4577a61-f377-3c08-93e4-256124c7e155 | -4.55689 | -42.97687 | 2026-09-19 11:25:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 83c7d6e2-cb9d-365d-947b-189952af9efe | -3.81685 | -42.22298 | 2026-09-19 11:25:00 | TERRA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 8b68a131-a894-37e6-a37c-d793712d7446 | -5.94873 | -38.12209 | 2026-09-19 11:25:00 | TERRA_M-M | SÃO FRANCISCO DO OESTE | RIO GRANDE DO NORTE | Brasil | 2411908 | 24 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 9a53a2d3-fb8a-386d-a6b0-84bfd8f81228 | -5.52019 | -43.7804 | 2026-09-19 11:25:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| af94645d-9613-3295-a2e1-9bc354d8eb79 | -3.10207 | -40.23857 | 2026-09-19 11:25:00 | TERRA_M-M | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 119e0b2e-f6aa-3cb8-bc57-5cfdd49a13b7 | -5.73586 | -43.50527 | 2026-09-19 11:25:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 58511086-0060-3dc7-824c-5cef514e4b5f | -5.65156 | -43.37918 | 2026-09-19 11:25:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 8043cd2f-ea89-3158-bb4e-d0c237b6fcca | -9.00776 | -44.92155 | 2026-09-19 11:28:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 93122862-c993-3ab6-8b4e-92e508cd20fc | -11.91288 | -50.10601 | 2026-09-19 11:28:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 084eb4c8-6510-31a0-81a5-fc53bf631d62 | -10.36667 | -48.89143 | 2026-09-19 11:28:00 | TERRA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| cbede6c6-0e6b-370f-9293-990ced302e6b | -7.01743 | -45.77242 | 2026-09-19 11:28:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| ba4e059a-2d23-3295-9ea6-138f52357654 | -10.48373 | -46.30189 | 2026-09-19 11:28:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2df6f2bc-cb5d-3594-836e-8887a01f62e2 | -7.59075 | -43.4429 | 2026-09-19 11:28:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 40723eb5-017b-371c-9a3b-bc9b46fc1638 | -10.5002 | -46.27754 | 2026-09-19 11:28:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| fd8c09b7-c3c7-3897-9e0a-35dcdf3ee1ec | -8.24221 | -45.60106 | 2026-09-19 11:28:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0358c94c-77b2-358a-8b42-64950548bbb9 | -10.54324 | -46.7284 | 2026-09-19 11:28:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 63af1837-5169-33af-af66-32bbbc29b424 | -7.80349 | -44.95427 | 2026-09-19 11:28:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| def1025f-35b0-3a6a-a505-d88198abb7b4 | -13.93298 | -41.43527 | 2026-09-19 11:28:00 | TERRA_M-M | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 4bec3ebd-7943-31d1-ab89-8658738b5780 | -7.86158 | -45.12206 | 2026-09-19 11:28:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 50.2 |
| a9a8b383-9659-3db3-afdd-9f6fd1923767 | -9.78923 | -45.06324 | 2026-09-19 11:28:00 | TERRA_M-M | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4954816c-45db-3fed-9d38-3e8cc7408fa7 | -7.37507 | -44.73038 | 2026-09-19 11:28:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| a84bdd73-acdf-3cfa-a57b-0df6aa40914d | -9.24834 | -45.94614 | 2026-09-19 11:28:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| e2483092-ade0-30c1-8bda-58e7a329162d | -10.13192 | -45.56173 | 2026-09-19 11:28:00 | TERRA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 26.1 |
| f1a8bcd6-59e6-3df6-833f-190aba3e0341 | -8.43602 | -47.74527 | 2026-09-19 11:28:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 000d2613-3e95-3910-af5f-1afbdea2ec19 | -7.01909 | -45.76127 | 2026-09-19 11:28:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| bcf6e416-5803-3a19-bcd5-a6d14ec1c4d8 | -13.01438 | -46.93347 | 2026-09-19 11:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| a2ee1c84-fb5a-3dde-a2c7-32915427eb49 | -5.94024 | -44.81617 | 2026-09-19 11:28:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f5c862af-efd6-310b-a85b-b68501f07c88 | -10.93222 | -47.85445 | 2026-09-19 11:28:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 58a40379-e931-308e-ba69-6e3d7ec6d191 | -8.45233 | -45.84827 | 2026-09-19 11:28:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 92a38048-2402-387f-9eb6-09ff60517610 | -11.08095 | -48.29656 | 2026-09-19 11:28:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| d9c65f41-1dda-305d-a343-2328de0ef519 | -10.80599 | -50.90106 | 2026-09-19 11:28:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 24.2 |
| b10d7129-e564-3ab7-a24c-18b8fb14db51 | -9.82607 | -46.39237 | 2026-09-19 11:28:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 59155f13-b16b-3eac-ae5c-16f0b01d2464 | -9.96017 | -46.58262 | 2026-09-19 11:28:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 818def50-a3ec-3fd0-a28a-8db973e2642b | -12.86704 | -46.34098 | 2026-09-19 11:28:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| ba0cf8e7-3d98-37f2-94bd-d64bbcd4a92d | -11.00705 | -48.32477 | 2026-09-19 11:28:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| aeb47cc0-c7d5-3c8b-9707-b1e50e4d745c | -11.31073 | -47.27089 | 2026-09-19 11:28:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 7dee9f25-9a22-3194-921d-1109f15aaf3e | -11.49579 | -47.72289 | 2026-09-19 11:28:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 9df4dccd-8357-35ed-b334-7cf34c7a6618 | -10.54145 | -46.74004 | 2026-09-19 11:28:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| b38cd65c-f22d-358e-8bb6-a3a6dfc222e2 | -11.00705 | -48.33131 | 2026-09-19 11:28:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 5080ac50-8d5d-3d5e-930a-3f62c2562560 | -13.0224 | -46.94621 | 2026-09-19 11:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 43882ae9-fd6d-3a0a-bde4-5caf71e36f8a | -9.36299 | -48.29878 | 2026-09-19 11:28:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 0e068d8d-b6d8-3c25-9f2d-53b741319e74 | -11.88054 | -47.62448 | 2026-09-19 11:28:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 37.7 |
| e1447879-8a66-3507-816a-cd3f472d6c9b | -7.98935 | -44.18715 | 2026-09-19 11:28:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e3ee683c-231d-329b-b1b9-87ee14b24d20 | -11.10944 | -49.44173 | 2026-09-19 11:28:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| a732caea-1be0-333b-9f07-7409bb94c76b | -11.92522 | -50.10126 | 2026-09-19 11:28:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| d820c222-c081-3262-b996-c8b64a942958 | -7.87096 | -45.12341 | 2026-09-19 11:28:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 21.5 |
| b0664533-2860-3eb5-b0a4-9cb083099a6d | -12.2773 | -49.17524 | 2026-09-19 11:28:00 | TERRA_M-M | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 17e76476-634c-3526-8858-85b8c571b687 | -11.08526 | -48.26895 | 2026-09-19 11:28:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 30.8 |
| f5bee4b6-e163-39b8-b5f5-579375840967 | -7.63198 | -44.73664 | 2026-09-19 11:28:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e84a4776-1a59-3d61-873d-c6d8cf74175c | -6.28811 | -41.77351 | 2026-09-19 11:28:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |


[Clique aqui para ver as próximas entradas](README102.md)

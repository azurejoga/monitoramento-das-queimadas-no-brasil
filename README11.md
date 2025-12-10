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
| 4f4d8297-e8ef-34bc-b236-42c1f1dd9e51 | -5.16039 | -44.10209 | 2025-12-10 04:36:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93d4bf3e-ec54-3a49-a8df-194fd05becc5 | -2.42108 | -45.84253 | 2025-12-10 04:36:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 26ac5e56-7526-33b8-976a-7b705ee751a5 | -2.28952 | -47.94529 | 2025-12-10 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 180b41de-a8e8-3fba-bc02-01d7b4632e18 | -3.69675 | -43.81086 | 2025-12-10 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 081e4e42-cc5f-3e61-a2c6-3a81aa1eb0dc | -3.22945 | -52.64454 | 2025-12-10 04:36:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d034b085-8f27-372d-9b0d-e367e925c679 | -1.67265 | -45.78081 | 2025-12-10 04:36:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9430923b-e5ab-3e39-8245-bb23d166b4db | -1.47853 | -54.20284 | 2025-12-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2b8ebc38-2e3a-37ab-8709-315c65f521b9 | -2.7759 | -54.52557 | 2025-12-10 04:36:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c5bd3cfd-7b05-3c33-b8f2-4d0e0d525515 | -2.28618 | -47.94476 | 2025-12-10 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82f3a14e-41c8-3017-a191-c861d66e32fa | -2.91374 | -45.34572 | 2025-12-10 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0c69859-bad3-3aa9-be54-ec217469ae06 | -3.23006 | -47.47759 | 2025-12-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d45593e0-2d77-3fa5-8e68-5793630227d0 | -3.55622 | -53.12705 | 2025-12-10 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60a6d6ed-e556-387f-8059-3fbf25ded59c | -4.5059 | -40.52045 | 2025-12-10 04:36:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6c02833f-77d3-36d0-bbbc-bc7b3a6437fc | -4.54421 | -45.90294 | 2025-12-10 04:36:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5c563fc-1dec-3b44-aa06-6957960dcede | -4.81103 | -41.82844 | 2025-12-10 04:36:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 331fc81b-f6fd-38b8-8af5-f55e7fe3228e | -3.18247 | -48.03178 | 2025-12-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 37c7a4e9-995c-321c-897d-1aaaaf4843c8 | -3.17969 | -48.02775 | 2025-12-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e840df54-541c-391c-b1a1-46a2e9dbb159 | -2.92738 | -48.22952 | 2025-12-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6fa63931-52f1-30f4-ab9a-e72d833e80ca | -2.9072 | -40.3458 | 2025-12-10 04:36:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d54b5e28-4c91-32db-9f00-b91351b30aaa | -4.34337 | -45.93594 | 2025-12-10 04:36:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b8243f0-db64-3be2-9b41-7a822ae2cab6 | -1.97182 | -45.86732 | 2025-12-10 04:36:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c95718c7-a2e5-3e54-ac91-c8cf36e736f0 | -1.08548 | -48.20835 | 2025-12-10 04:36:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f134d002-afd1-3dea-8bd4-af78fe6ac574 | -8.1546 | -43.17572 | 2025-12-10 04:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5db9f02e-e0d2-3c93-995d-351df685842b | -11.11422 | -40.27765 | 2025-12-10 04:38:00 | NPP-375D | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ba15a05f-966e-37d2-a76c-a0314c0c40f6 | -7.0479 | -45.05233 | 2025-12-10 04:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 32e15774-cc3e-3962-bd0e-f78327512a8d | -6.89993 | -42.8381 | 2025-12-10 04:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 059521e1-dc01-3bae-83b0-b2bdcc5a86f3 | -8.09947 | -55.01043 | 2025-12-10 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 767388ac-5ea5-3220-84ec-53e0a5fea4cb | -6.54432 | -43.60329 | 2025-12-10 04:38:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c775da45-d157-315f-bfd3-f988fc25289a | -6.52288 | -41.57371 | 2025-12-10 04:38:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 81695de5-1442-380b-9e82-0eb6050b780f | -8.67231 | -44.21996 | 2025-12-10 04:38:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a311301a-e1db-3c0c-adb8-5e35619ad728 | -6.94312 | -38.61045 | 2025-12-10 04:38:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a17f6e77-1273-3f1d-a5a5-56f3f9d20c3d | -6.94361 | -38.60685 | 2025-12-10 04:38:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 961d4cd5-5ce8-3ad1-82d2-8ddf92077741 | -10.98979 | -53.9986 | 2025-12-10 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85bc8637-7f90-317b-ac2d-33724ebbba67 | -5.27657 | -49.52961 | 2025-12-10 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f7d71f4a-e317-32ab-aca2-5899373b2c78 | -11.10861 | -40.28023 | 2025-12-10 04:38:00 | NPP-375D | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 83acad8f-7e50-3f60-8904-6456ff664982 | -8.66776 | -44.22416 | 2025-12-10 04:38:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 09a55fbb-4f78-3a5c-812e-f08a914c6ef4 | -8.15919 | -43.17273 | 2025-12-10 04:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 34e99dcb-979b-3cae-9bf2-033bec328e3e | -6.89532 | -42.84105 | 2025-12-10 04:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a1e5e843-cd3e-3135-8bc9-53c1d4087296 | -7.17521 | -35.99962 | 2025-12-10 04:38:00 | NPP-375D | CAMPINA GRANDE | PARAÍBA | Brasil | 2504009 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cc0f3065-884f-3ae5-b0a6-2e23aa1b408b | -8.09868 | -55.01489 | 2025-12-10 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa36b237-78f4-3264-bfc9-f07350970640 | -6.54449 | -43.60504 | 2025-12-10 04:38:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7019ffc-eb16-3f37-af52-31a5eac51cad | -6.68794 | -43.68661 | 2025-12-10 04:38:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c27e58e1-6c17-3cb6-b4c6-6e1af2cb8281 | -6.54851 | -41.70921 | 2025-12-10 04:38:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0585c5de-e0bd-3756-be08-cc9a48df02fb | -9.08599 | -40.87599 | 2025-12-10 04:38:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d5160664-29e1-329a-814e-b91a29d73a27 | -9.82052 | -47.93286 | 2025-12-10 04:38:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eec4ca64-ca17-3661-8d6c-f2f723357535 | -11.11381 | -40.28086 | 2025-12-10 04:38:00 | NPP-375D | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f8517a87-5827-3245-87d6-f84a635795be | -7.12496 | -39.99345 | 2025-12-10 04:38:00 | NPP-375D | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b61a4114-1179-34a2-bd3a-88b4b9b2604c | -7.1817 | -36.00048 | 2025-12-10 04:38:00 | NPP-375D | CAMPINA GRANDE | PARAÍBA | Brasil | 2504009 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 601d1cce-f993-366b-a585-a73135b4f4fd | -8.50956 | -43.32687 | 2025-12-10 04:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 9aadc286-d65f-3849-9ba6-98c9da779995 | -9.08718 | -40.8807 | 2025-12-10 04:38:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 21d1af3a-cb0e-325a-9ef5-832c0e7fb423 | -6.93208 | -42.64571 | 2025-12-10 04:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d08a2ae8-2884-3c81-9239-f7b2158936c6 | -6.7633 | -44.21003 | 2025-12-10 04:38:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f003bb4-0ea0-3d2d-a538-960e1e72e2c7 | -11.10902 | -40.27702 | 2025-12-10 04:38:00 | NPP-375D | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d56ebb10-4527-3c0c-b7ec-33458afe6c54 | -8.50498 | -43.32985 | 2025-12-10 04:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a1542c50-690c-357b-a9b7-be26262d5ab8 | -6.89584 | -42.83743 | 2025-12-10 04:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 691e9242-00bd-3d85-a580-941b510b827b | -8.15867 | -43.17635 | 2025-12-10 04:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 58f4fa36-73b9-34d0-9cb8-fc24a9cb0867 | -6.23079 | -44.16454 | 2025-12-10 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c947925-748a-303a-8bf1-5992af282243 | -7.11999 | -39.9926 | 2025-12-10 04:38:00 | NPP-375D | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5ebc16cd-9e65-3136-8106-b45cb9a83a6e | -7.78127 | -42.00171 | 2025-12-10 04:38:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 712781ab-ec1b-32bc-8c5d-98650402df2c | -8.66845 | -44.21949 | 2025-12-10 04:38:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 15cc1da1-f8e2-3206-9695-a40531de67cd | -21.97643 | -56.79226 | 2025-12-10 04:42:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1f0c87a-51b6-3fbe-9f03-5eb47944169c | -20.91727 | -56.38044 | 2025-12-10 04:42:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e54a82a-f766-37f1-afee-89e39644f1a5 | -21.97248 | -56.79134 | 2025-12-10 04:42:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad2e7942-26c1-30f8-9dc8-1775f4b50e78 | -0.87664 | -52.62067 | 2025-12-10 04:55:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9830184-fbb4-34c2-8952-daf55900d22f | -1.01696 | -53.73388 | 2025-12-10 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 51d2a83a-e958-3d9d-b185-faf0f022071d | -0.96713 | -53.08142 | 2025-12-10 04:55:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2d58441-1c80-32f2-90bc-1807ccd71c14 | -2.90911 | -40.3461 | 2025-12-10 04:55:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7b47af7c-ccf1-3040-b9f2-0b40ca1cfb80 | 3.38081 | -51.26443 | 2025-12-10 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 674d7681-40fe-3eb3-93fd-952d6d44e6dc | -2.05938 | -46.50023 | 2025-12-10 04:55:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 78a38b61-5329-35b8-9f54-06e2d67be683 | -2.90817 | -40.35253 | 2025-12-10 04:55:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 714ef343-98c0-36ff-acb8-d86d77e678fc | -0.99168 | -52.32374 | 2025-12-10 04:55:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b93a811-8b2a-3a8e-b673-104ebfc77085 | -1.08883 | -47.26701 | 2025-12-10 04:55:00 | NOAA-20 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db9e31c9-a613-34b8-9b93-5046c65a73b7 | -0.90519 | -52.46285 | 2025-12-10 04:55:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58ce0c03-5991-30da-b439-fed37cb67831 | 0.61096 | -51.56549 | 2025-12-10 04:55:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bcc5071b-9895-3faa-883b-404f5b811828 | 2.03038 | -55.67395 | 2025-12-10 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f9e6d4c-48be-333a-9a8f-e0992094118a | -1.75719 | -45.51692 | 2025-12-10 04:55:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e3654d8e-76b7-3cdd-8c55-9d86746f80dc | -1.11236 | -53.68881 | 2025-12-10 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d89c64c4-70b0-3c99-a740-c2abce2717a9 | -1.53467 | -49.44336 | 2025-12-10 04:55:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5663ab0-445b-3fea-abaf-3b3877d54be2 | -0.97363 | -52.43805 | 2025-12-10 04:55:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6a3bdf3d-25ac-3050-8a69-5c534c3d2702 | -1.08943 | -47.26308 | 2025-12-10 04:55:00 | NOAA-20 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 472684e2-a7ac-3fde-a569-73e9b62d68e7 | -1.24143 | -52.87158 | 2025-12-10 04:55:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bc9d3818-2dfb-3b97-b545-d2cc64d7aa04 | -1.73467 | -46.51191 | 2025-12-10 04:55:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2116da5b-6de0-30d1-884c-e8626dc51fbd | 0.5877 | -50.80136 | 2025-12-10 04:55:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 746b5bba-c8d9-33f7-915f-c3b92804f88b | -0.80549 | -48.12721 | 2025-12-10 04:55:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 340db9d3-26a0-304a-92c9-70b1ce663968 | 0.61152 | -51.56901 | 2025-12-10 04:55:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c224b42-28f1-3a2b-a69c-70a23864e0f7 | -0.9764 | -52.44202 | 2025-12-10 04:55:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adadbb49-ddde-3a4c-a31a-b918b89d5187 | -1.84558 | -46.39933 | 2025-12-10 04:55:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bae5b81-e0c6-3afd-bdae-8a1a40d4cd52 | -0.84225 | -48.11156 | 2025-12-10 04:55:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90906080-e467-39e3-829a-f278b254f90a | -1.3446 | -47.34951 | 2025-12-10 04:55:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22f35a6c-873d-3e4f-bb39-aad5fe003f52 | -0.32515 | -51.70308 | 2025-12-10 04:55:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1e9e56ce-dfe2-3a22-ab1f-49016585e640 | -1.84575 | -46.39654 | 2025-12-10 04:55:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cc46d9b-3e8c-364d-a317-bb6830c2555e | 2.01757 | -55.66315 | 2025-12-10 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0b01ebf-06a6-3f26-b712-f5b18d1c9d6d | 3.37748 | -51.26495 | 2025-12-10 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7218c4b5-e2ab-3b19-94f3-c08f6c3eb793 | -1.01751 | -53.73043 | 2025-12-10 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fa82d1a5-29f1-3713-9cc6-ffd2b2c397d3 | 3.37527 | -51.27244 | 2025-12-10 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12ed33e2-b1d3-354a-838f-ffbee9296784 | -1.01643 | -48.16381 | 2025-12-10 04:55:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a4ee0b1a-7b1f-327d-83b3-1a7a1a405c7e | -1.10904 | -53.68829 | 2025-12-10 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b9eb357-15d5-3d8a-919a-0e4915d49bd7 | 3.37804 | -51.26844 | 2025-12-10 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e0ea6e8-e128-3c1a-850e-0fc9cb42e39e | -1.73398 | -46.5094 | 2025-12-10 04:55:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c501ca5-ab1f-3cd1-a04b-2e64bfb37cbb | -0.90573 | -52.45939 | 2025-12-10 04:55:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README12.md)

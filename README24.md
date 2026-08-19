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
| da11b9b7-5a8d-32a8-8353-39a56cf45dd6 | -12.52637 | -47.84115 | 2026-08-19 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da124c99-c9d5-3d72-8d8e-bc754314dbe2 | -11.20721 | -54.01244 | 2026-08-19 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 303b079f-7e87-36ea-a05b-708079b8e6b3 | -8.35936 | -45.97544 | 2026-08-19 04:19:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b1721772-f888-3f02-9e9d-89a9abafc3e9 | -11.3848 | -46.38983 | 2026-08-19 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c6f5c33-d06e-3831-9f9c-7a4b8e3f0ca7 | -8.57375 | -54.7757 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 204d8e18-9f40-3235-a416-cf93bd33d72a | -12.75685 | -48.44497 | 2026-08-19 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71bd8bc8-7da6-32db-96ea-aba8e5c62de3 | -11.15576 | -49.62383 | 2026-08-19 04:19:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d44ff08-0eff-318f-905f-fdeba5bec04e | -6.34981 | -54.91278 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db6fdb00-73da-329c-90d1-cde19c143822 | -8.58647 | -54.72512 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b601582e-b2d3-300d-8c48-fa1c2e70fd64 | -8.5843 | -54.73639 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d295d7df-ed79-3ecb-84c1-75c68fe1393f | -11.05776 | -46.5127 | 2026-08-19 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e10d9916-9a05-3a70-8906-54e8e35fcaac | -7.53836 | -55.59642 | 2026-08-19 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28260ab1-efa5-3171-90ad-37f3313b11a4 | -12.79272 | -48.43294 | 2026-08-19 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 726787b9-d09d-3184-9234-4b17c7811fae | -8.17858 | -44.43232 | 2026-08-19 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 47c6b3f0-41e0-377a-8f60-1a140b4832fc | -10.2813 | -48.23554 | 2026-08-19 04:19:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce0f851c-40bb-3701-a3e3-31c6240dc073 | -8.50491 | -54.86289 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c6cf629f-c448-3b62-b3c5-13e80d74fc56 | -11.02075 | -45.24643 | 2026-08-19 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f7ec63d-f2e1-3d06-b6ad-78cdd4731604 | -11.2054 | -54.0214 | 2026-08-19 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 345124c3-00ee-372a-b1db-6d092ad83f7b | -11.23056 | -55.07629 | 2026-08-19 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4351585a-ae4e-3e11-aae7-7662e0e1a494 | -6.44395 | -52.72809 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ffedf4e-9877-318b-8ec5-fcc2b299ec8a | -12.23638 | -43.15268 | 2026-08-19 04:19:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4612f0a2-1bb5-3278-b4d1-d3f62795201b | -9.46138 | -51.60735 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 347a6960-0bd0-3795-9f67-c7f78dad1a7b | -7.56586 | -55.56705 | 2026-08-19 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ee7eb54-2bca-3cb7-b450-f078cce4e1ee | -12.51755 | -47.84492 | 2026-08-19 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f04af303-7098-3323-8dc0-7f0b0c02ff51 | -12.3726 | -46.44957 | 2026-08-19 04:19:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c57e962-cdda-3533-b358-629d534bc67a | -9.74495 | -43.30393 | 2026-08-19 04:19:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6a272320-3762-3145-92f4-de8b9fb68003 | -10.24609 | -46.99458 | 2026-08-19 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b76d2596-25f1-3347-bdb4-9de1e125be94 | -9.8126 | -46.62263 | 2026-08-19 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 08915a05-a22f-3747-9938-84ec1e599c49 | -7.17618 | -43.10916 | 2026-08-19 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c486c1f4-c62f-3fcf-93a5-d182bba8051c | -8.57723 | -54.75822 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 72a33293-141c-38ad-ae0b-b3563058dac4 | -11.2231 | -55.08202 | 2026-08-19 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9331d7aa-b017-3eb2-98c2-ceba6671605e | -6.44064 | -52.74606 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9de047b-ead1-31cc-8746-5bc8abf46e2d | -12.77246 | -48.45217 | 2026-08-19 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fdb02c63-c56f-376d-94f5-964a14924b0b | -12.95464 | -41.82193 | 2026-08-19 04:19:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a4578f67-8dc5-3b7a-9454-8333fa6c05c6 | -8.55481 | -54.74761 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bd7d9fb3-f00c-37d3-bfe2-445dd2db76c6 | -7.45438 | -45.14466 | 2026-08-19 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 393eddbe-0309-3370-a767-de3310d1a8f5 | -7.17338 | -43.10503 | 2026-08-19 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ffa36af4-ff65-33c1-ac96-59d0adb463b1 | -11.20487 | -54.01894 | 2026-08-19 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25f17ea6-128b-37b2-a360-bbb7ccc334fc | -6.44998 | -52.72923 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8fa27b0-f167-3e76-9937-662ed689b02b | -6.16501 | -47.7588 | 2026-08-19 04:19:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f04481cb-8855-30b4-b39c-f75a7ed2dee4 | -6.45161 | -52.72033 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff30914d-72ee-3a2d-ad09-b23a80f27945 | -6.45079 | -52.72478 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 182fb4b0-7a9c-39f4-b2ef-c4bd755e29b4 | -11.23932 | -55.0682 | 2026-08-19 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb3bebf6-db1c-3359-8176-4576460416f8 | -10.67676 | -49.00132 | 2026-08-19 04:19:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53fc139b-b8fe-3f12-8d8b-480c23212f7f | -7.62906 | -45.71767 | 2026-08-19 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f147e32-f893-37ce-a09b-8527319e992e | -11.49214 | -45.10554 | 2026-08-19 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b136d8e-5e57-3ff7-8b46-2d35008823c8 | -11.20029 | -54.01565 | 2026-08-19 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e43c5a51-5b85-3a58-b1be-298eab7e2a51 | -11.22631 | -55.06401 | 2026-08-19 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08932c42-ceeb-34c9-b3e5-bfe922436aa9 | -12.25241 | -43.15892 | 2026-08-19 04:19:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f0ae4520-2d49-341a-9fe7-6c3d10e540f4 | -12.24853 | -43.1619 | 2026-08-19 04:19:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| df765420-0cfb-3eee-8598-505a7af1defa | -9.73059 | -46.77613 | 2026-08-19 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd19abf8-f594-33c5-ac36-1d1d907a5655 | -6.35838 | -54.90723 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6bca0455-0248-3995-afa7-474889767b92 | -10.2422 | -46.99393 | 2026-08-19 04:19:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dcebbf3d-6782-3ed2-b339-960375c5b23c | -11.11842 | -47.26279 | 2026-08-19 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0dba1d5f-9dd6-32c9-8526-008500ad8b68 | -10.64656 | -51.61017 | 2026-08-19 04:19:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5f6fdf82-c26f-390f-8560-cc7fad9735d4 | -8.53279 | -54.75531 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 22cb76b2-92cc-3607-9836-09c2d1d4b98c | -13.44014 | -43.83892 | 2026-08-19 04:19:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e7cbdef-f154-3c37-a752-f4dcedd036a6 | -7.3467 | -44.37689 | 2026-08-19 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4530e04c-15b8-35a9-8ff7-b7fde32aa913 | -7.94321 | -44.63594 | 2026-08-19 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0a1dbcdc-c191-38f8-8427-6c8f6ce71853 | -8.35108 | -45.97877 | 2026-08-19 04:19:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 14168ab6-5a03-3557-9e17-4b0e3f4ce966 | -9.72889 | -46.78584 | 2026-08-19 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5e016128-00fa-313d-8d78-85b09d91e119 | -8.36271 | -46.34795 | 2026-08-19 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1eff40ae-0952-3dcf-8675-b34f9e7a1ffa | -11.69123 | -54.55599 | 2026-08-19 04:19:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1ee8ae93-9c37-33f5-81ab-5096d27995ec | -11.24039 | -55.063 | 2026-08-19 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 423691eb-1b74-3be6-b25d-7ebf02cb4fde | -12.82716 | -48.42088 | 2026-08-19 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a4633b1-7e99-3d75-ad42-87faaba65cff | -6.26935 | -53.56669 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b9715a1-e5fe-30dc-bd1e-129da5754905 | -12.18992 | -45.15274 | 2026-08-19 04:19:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00b494ad-173c-370b-86bb-77a9b2d2abb9 | -8.5395 | -54.72091 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3ed7eefd-8e55-3e2c-aa27-a388945b195b | -9.06137 | -50.85873 | 2026-08-19 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62306e55-7416-3b9f-af21-b6c1e47e5ef0 | -9.46201 | -51.60397 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3595b578-07e3-3a78-b8f3-0bdf24b709c7 | -9.73574 | -46.8379 | 2026-08-19 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa4b89db-c1fc-39fc-92c4-fe445c4f1760 | -8.53717 | -54.76796 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 37d7bb63-ae7a-371b-8b6d-4efe3d0bb58a | -9.45466 | -51.61376 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ebbaec0-fdd5-34e4-8c69-caceb4cde168 | -8.5526 | -54.72374 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7436801a-f769-3582-9d7d-940e8400c790 | -8.36191 | -46.35272 | 2026-08-19 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 60888db6-5cbe-3618-9cd3-3e8ca05e2883 | -8.54372 | -54.76953 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5cbc3bc4-50c1-32c6-a4e6-eff5533934e9 | -11.21265 | -54.01117 | 2026-08-19 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46fb5b61-8d87-3d83-993a-e3b02115c19a | -13.44347 | -43.83946 | 2026-08-19 04:19:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56802a5f-d7e6-3b9b-8683-8709bfa227c0 | -6.34294 | -54.91144 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b5609888-b21e-3680-8579-3ea63f90b4e0 | -8.35484 | -45.97939 | 2026-08-19 04:19:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d11028d6-c59d-354b-acdc-007938a4dcfd | -8.58549 | -54.76582 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 49cd6755-bd48-3a6a-acc7-dadf98fd0232 | -11.64061 | -54.53156 | 2026-08-19 04:19:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b17fd13d-f52a-3f39-ad96-fc273cb68463 | -11.22947 | -55.08181 | 2026-08-19 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5f2e5574-6384-3eac-a565-8e62b8573d23 | -11.48801 | -45.10888 | 2026-08-19 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f07749c-4bd5-3984-bfba-acc74a8e208f | -11.2212 | -55.05876 | 2026-08-19 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22d583f7-aae7-3c88-b12d-ed2bdc2ce9eb | -9.45803 | -51.62535 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 170924d6-809f-3eb6-83d9-37d4be7ec20b | -11.22651 | -55.06546 | 2026-08-19 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 836b6fb2-25a7-37c4-9e9d-eb0c6dc2359e | -11.21353 | -54.00665 | 2026-08-19 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 281735a2-7416-3cf2-8de9-536a46c6baa2 | -11.71542 | -54.62804 | 2026-08-19 04:19:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fe9c7bd-8743-3f88-bcea-b03eaea66305 | -8.5273 | -54.74841 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6bb102f0-eada-3c6a-bdd3-68594b09f2ec | -7.53395 | -55.58152 | 2026-08-19 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ad17c41-234c-3246-96c3-2c348781c130 | -8.53836 | -54.72674 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3630c1fd-933c-37da-97a4-3e5bb95555f4 | -6.26303 | -53.56519 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 877d79ae-cb48-37ea-af18-4939578a87de | -6.39604 | -51.75181 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 323bf738-7c7d-351e-9d47-08be1f51fa78 | -8.54917 | -54.77673 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8923e22a-3bb1-37f1-a8e3-579bf39dbc96 | -8.58825 | -54.73724 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d23efb08-d40f-3741-ae9f-bd4332f10d64 | -8.56044 | -54.75384 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6eca7b84-5292-30cc-80b3-62c590236c26 | -8.5503 | -54.77089 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 624d4b26-29e0-3185-a863-86104a1cff38 | -7.17001 | -43.10448 | 2026-08-19 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fb84ff2c-ba9f-3ba7-a130-d4ae8ffcf9f8 | -12.24077 | -43.16788 | 2026-08-19 04:19:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README25.md)

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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d77002c-6e57-36d0-8ec6-cecdbfe901d8 | -11.79012 | -47.37177 | 2025-05-16 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bcae74bf-d12b-3c35-8ae6-68828a297fcf | -12.62859 | -54.87206 | 2025-05-16 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea322e4c-2e90-36db-99e2-22c74ea6b69c | -11.78267 | -47.35144 | 2025-05-16 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5765787f-b548-37e2-92cc-0b2b7c0f3877 | -13.04134 | -53.71538 | 2025-05-16 04:36:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06f79efe-13aa-37a5-97fa-6b353fa3cc57 | -17.79801 | -44.35869 | 2025-05-16 04:36:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62f8aae7-de5e-3b15-bf17-4343e370daad | -11.55359 | -47.61477 | 2025-05-16 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9da2b31-5aa7-3144-b24e-17d01fc62475 | -12.12154 | -54.66469 | 2025-05-16 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d20e84d2-496c-370e-a568-41edacff822d | -12.87181 | -55.0652 | 2025-05-16 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8618bef7-cd4a-35f0-95f7-5f8ba4903b6d | -16.68208 | -43.88387 | 2025-05-16 04:36:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8b6fb25-65e6-3883-b52b-3f72fca3eddb | -12.34348 | -49.95526 | 2025-05-16 04:36:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b475b3f-8ec4-38bb-a188-6edeb580e5ca | -12.45121 | -57.20753 | 2025-05-16 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2e98e03-b80f-3448-8f6a-8e0428e6b5be | -11.63283 | -48.02849 | 2025-05-16 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d44d8a20-ccde-36f1-94c4-dbfd14874c5b | -12.34567 | -49.96296 | 2025-05-16 04:36:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46ee040b-65fe-346d-aaf1-1a870ed0b504 | -13.96004 | -56.79134 | 2025-05-16 04:36:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74040430-4162-3d21-b99e-b97b4bde89f6 | -14.16791 | -45.47041 | 2025-05-16 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 50488d7d-516d-3c0a-83c2-f3ea09aeaaea | -11.58187 | -47.6117 | 2025-05-16 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7d4068f-31e6-38d6-b1bb-c1a097161895 | -11.57452 | -47.61432 | 2025-05-16 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 69f5564b-d8a5-37f6-bc0d-82b8ed22ca92 | -17.79853 | -44.3545 | 2025-05-16 04:36:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 316adfd3-f359-3455-912f-94dbe54d79d5 | -11.58131 | -47.61537 | 2025-05-16 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d07fa1e6-5393-30f7-8db6-2e71f24c03b8 | -13.98032 | -56.80189 | 2025-05-16 04:36:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d75b68d-d144-3aaa-9b2c-b54167bfa633 | -15.26369 | -51.4621 | 2025-05-16 04:36:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3de86526-423c-3af4-a576-9381454ef47d | -13.59576 | -47.37403 | 2025-05-16 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71703471-e5b6-35fa-a3bf-36bb94c499d1 | -10.463 | -54.98403 | 2025-05-16 04:36:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28d59e64-ccb8-32b0-a661-61c0b9d8dc99 | -11.55699 | -47.6153 | 2025-05-16 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2286dafe-25af-31cc-bada-0e5984bc1a34 | -11.6527 | -58.26371 | 2025-05-16 04:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c119b773-4539-3715-96be-4369256c8a06 | -14.87056 | -51.97821 | 2025-05-16 04:36:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c57b33da-bff3-3cca-9f44-d9d8270f4166 | -22.04373 | -56.64561 | 2025-05-16 04:38:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2b95043-0d0e-39b5-bf53-14f0df4620d1 | -21.58277 | -53.81244 | 2025-05-16 04:38:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4e6eaec-daaf-3042-99fe-1983b5239814 | -18.14497 | -47.8033 | 2025-05-16 04:38:00 | NPP-375D | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9697920-8158-3410-a924-2567a9bc809c | -18.33212 | -51.45969 | 2025-05-16 04:38:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f6eae3b-79dd-367a-83b0-955833bb2a45 | -19.06582 | -53.45477 | 2025-05-16 04:38:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 68d0f5df-1e2b-3986-8cff-6f68954e730a | -19.45524 | -45.30453 | 2025-05-16 04:38:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53abacac-1625-33ac-a932-32ae11a7b9d7 | -16.9395 | -53.44929 | 2025-05-16 04:38:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbda938f-b83e-3710-a481-6784da830d9a | -20.47626 | -53.67759 | 2025-05-16 04:38:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d8f9653-9cd7-36ca-87a9-9a23fd262f0e | -23.07443 | -50.3461 | 2025-05-16 04:38:00 | NPP-375D | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b573c2eb-f95c-3a11-bd58-3e41edaab386 | -24.41237 | -51.34019 | 2025-05-16 04:38:00 | NPP-375D | RIO BRANCO DO IVAÍ | PARANÁ | Brasil | 4122172 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 239be080-c466-38e3-adc5-f2f52f1211a2 | -17.48529 | -53.83493 | 2025-05-16 04:38:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0022aa9-3786-3a57-8608-90e8dc8edf76 | -20.18948 | -55.03967 | 2025-05-16 04:38:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb74fe97-cf2e-3427-b2f5-9fd00f318159 | -23.29033 | -51.59922 | 2025-05-16 04:38:00 | NPP-375D | SABÁUDIA | PARANÁ | Brasil | 4122701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2a87906c-8783-3028-ad30-a46843ffbaf4 | -20.7626 | -46.76722 | 2025-05-16 04:38:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 41634c6b-edcb-3316-a6e3-4346ed34cef6 | -17.48241 | -53.82987 | 2025-05-16 04:38:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c184ee64-8bd7-30f8-82fe-119857e9bdb5 | -22.90219 | -43.7564 | 2025-05-16 04:38:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| afbe08b3-2496-3c2f-baf2-8dc92af11c0f | -23.57135 | -55.00527 | 2025-05-16 04:38:00 | NPP-375D | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 45ba7814-5aa0-3dd4-9f03-21b62d514ba9 | -19.06302 | -53.44997 | 2025-05-16 04:38:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 48965a72-b2f6-3dca-b16b-68abb19f2fe4 | -20.25559 | -49.34525 | 2025-05-16 04:38:00 | NPP-375D | ORINDIÚVA | SÃO PAULO | Brasil | 3534203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 28ec3e74-f14d-34d6-a017-f12457c8bedf | -25.19238 | -49.32632 | 2025-05-16 04:38:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2a8d6c51-f84d-3458-8375-58f2c0d67aae | -21.13011 | -55.97278 | 2025-05-16 04:38:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 911908da-3ba7-34ef-af3d-a68cbee9c450 | -23.42169 | -52.30023 | 2025-05-16 04:38:00 | NPP-375D | SÃO JORGE DO IVAÍ | PARANÁ | Brasil | 4125308 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| b9ae16a5-e2eb-3dfe-b78f-894abec02ba4 | -16.93765 | -53.45176 | 2025-05-16 04:38:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33b6fe1e-bd0e-3f54-929c-dea7afffc8ea | -20.76305 | -46.76831 | 2025-05-16 04:38:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4a69031e-3ff1-394d-b4ba-2e8bd97179c3 | -19.1618 | -47.81866 | 2025-05-16 04:38:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae3ed79c-e29c-3d1e-87cd-af90b4dcfd8a | -17.48318 | -53.82547 | 2025-05-16 04:38:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f2da354-7d37-329f-83fc-eed3778ef83e | -23.98284 | -48.91707 | 2025-05-16 04:38:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 886349cc-50cd-3064-8db0-8302ae01f0ea | -18.33665 | -51.45291 | 2025-05-16 04:38:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6e3113c-c029-30c2-82fc-44e981086172 | -19.53179 | -43.91911 | 2025-05-16 04:38:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe0e4e04-1487-3dd0-82ce-6a2e62875cd9 | -24.64079 | -50.86804 | 2025-05-16 04:38:00 | NPP-375D | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 74c3c8f7-8b4e-3d22-92c7-b2e00dc5a363 | -19.02265 | -57.61961 | 2025-05-16 04:38:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| df83c81f-7a7d-3b07-819a-10f5fa545dd9 | -19.96928 | -44.21435 | 2025-05-16 04:38:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5543f3ef-bded-3666-ad56-0b4d99ff20b8 | -19.26141 | -48.73071 | 2025-05-16 04:38:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5f8efeac-8952-30f9-8623-4ef612af3e5b | -19.06231 | -53.45409 | 2025-05-16 04:38:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 13.1 |
| dd4091d6-34de-3a4d-9262-a521278a2d8d | -19.456 | -45.30679 | 2025-05-16 04:38:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3b37837-67ee-32d5-b85b-07f62371014d | -21.23923 | -44.16423 | 2025-05-16 04:38:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5f202e25-b5c9-3e0d-9ef3-c5385d7ddfc3 | -18.33606 | -51.4566 | 2025-05-16 04:38:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b1835fe-96aa-3629-87df-ce556197f29b | -20.18863 | -55.04442 | 2025-05-16 04:38:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5a2259c-2764-3a32-82a9-9bdfb72acb79 | -21.5793 | -53.81177 | 2025-05-16 04:38:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 717bd0ef-0e94-3968-af36-9ba9f15b7355 | -19.06653 | -53.45065 | 2025-05-16 04:38:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 397de3eb-1ded-36cf-a515-bc10d5d473f9 | -20.47599 | -53.67787 | 2025-05-16 04:38:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07380f0b-ec25-3a0b-9e68-88142090f06f | -19.02177 | -57.62411 | 2025-05-16 04:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f018ac42-ec03-3c50-bf82-de6a16319ecb | -23.4223 | -52.29645 | 2025-05-16 04:38:00 | NPP-375D | SÃO JORGE DO IVAÍ | PARANÁ | Brasil | 4125308 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| fc91b5db-f990-3d56-bff7-e9c3c8e60a02 | -19.15878 | -47.81398 | 2025-05-16 04:38:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f7505490-8fff-3efd-8742-45768da72ab4 | -23.28699 | -51.59861 | 2025-05-16 04:38:00 | NPP-375D | SABÁUDIA | PARANÁ | Brasil | 4122701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c8df4d4e-545d-314e-854a-cd291cdb8912 | -19.1159 | -52.70727 | 2025-05-16 04:38:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1db2e017-76d4-3b34-9504-1dc327a7b039 | -19.15819 | -47.81819 | 2025-05-16 04:38:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3d8278c-937b-3244-a338-93babb5b4807 | -20.18575 | -55.03895 | 2025-05-16 04:38:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 11b03186-f048-3d52-b2a1-d60f1c897d8c | -25.1848 | -50.10563 | 2025-05-16 04:40:00 | NPP-375D | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4a7b6d00-2d48-32b5-96a0-6efbc4103c30 | -29.79358 | -54.65867 | 2025-05-16 04:40:00 | NPP-375D | SÃO VICENTE DO SUL | RIO GRANDE DO SUL | Brasil | 4319802 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 51935cad-9697-33bc-933d-f075c9d4f146 | -27.11795 | -50.57251 | 2025-05-16 04:40:00 | NPP-375D | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7bad0299-4dc3-3917-a166-360f07b97ae4 | -28.74348 | -49.38392 | 2025-05-16 04:40:00 | NPP-375D | CRICIÚMA | SANTA CATARINA | Brasil | 4204608 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 74c1b2a8-e59a-36ba-891d-92251560705f | -27.11448 | -50.57192 | 2025-05-16 04:40:00 | NPP-375D | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7221923b-3bae-382a-ad53-f40fc2d9c7b6 | -28.55775 | -49.00498 | 2025-05-16 04:40:00 | NPP-375D | JAGUARUNA | SANTA CATARINA | Brasil | 4208807 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| fabff79d-8902-3002-810c-9bbc7198e151 | -26.27527 | -50.39032 | 2025-05-16 04:40:00 | NPP-375D | CANOINHAS | SANTA CATARINA | Brasil | 4203808 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f989e9ad-b855-30fc-8f14-91cdb8cf0dec | -6.6613 | -43.19412 | 2025-05-16 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d250f8fb-866b-3b85-8e43-8dcbde2923e6 | -6.71771 | -47.59063 | 2025-05-16 04:55:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f18b49e-920f-327e-837e-7eadb28a628e | -9.3713 | -48.39734 | 2025-05-16 04:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f739d03b-ea84-35ba-9bc9-ecbcee4902f0 | -7.07532 | -44.38847 | 2025-05-16 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01df1b9d-089b-36c4-8cc1-50e52c22f0ca | -6.66019 | -43.19172 | 2025-05-16 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3478c327-ec3a-359e-999c-2896f4fd7239 | -8.43064 | -46.63862 | 2025-05-16 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8e2bd336-6470-38ef-aee0-4afa6ca2003d | -7.74209 | -46.32598 | 2025-05-16 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6bef110f-2746-3e8c-bb70-e90265914044 | -7.07709 | -44.91415 | 2025-05-16 04:55:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da9246ce-2504-3b97-b2f4-dfd49425bf0e | -7.07481 | -44.39224 | 2025-05-16 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b616bf4-8e7f-307c-a644-8d519aba0fcb | -8.26535 | -54.96361 | 2025-05-16 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9770d00-ac2d-37f3-99ce-6bb588ad7a11 | -6.65954 | -43.19637 | 2025-05-16 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 15ff2fd3-72cb-32c0-bc6c-799bd27c75f6 | -9.37189 | -48.39939 | 2025-05-16 04:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9973090e-30dc-3937-9fef-7d36d52a47cf | -5.77748 | -43.61549 | 2025-05-16 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9709875e-22d1-3a98-964c-ac60a3431aa7 | -7.45566 | -49.77399 | 2025-05-16 04:55:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62aab5a1-ceab-3dc7-811a-261ef29e3f4c | -8.42882 | -46.63784 | 2025-05-16 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1feb1200-caf0-34c1-8796-7dd25079ac6e | -9.36747 | -48.39872 | 2025-05-16 04:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75666cd9-38fe-3fd0-8f46-748e2193de69 | -9.36685 | -48.40311 | 2025-05-16 04:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4d38d78-3f9f-39b4-9a6d-39a3c38e7597 | -10.006 | -47.84141 | 2025-05-16 04:55:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9115ed88-d432-3007-b4fd-304cce4b0cae | -7.45514 | -49.77504 | 2025-05-16 04:55:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README10.md)

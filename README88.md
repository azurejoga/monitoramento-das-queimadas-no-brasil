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
| a84d6790-d4d2-3e79-a541-3a30d01f3710 | -12.622 | -56.99926 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a180e46-3d84-30e1-8696-d5a9b4e54b72 | -14.40807 | -51.7028 | 2025-09-03 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5970e548-0d20-3435-8fd1-6914c1b04ced | -12.99218 | -48.08697 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db21c015-7b00-3ada-874c-bb8c1e286865 | -6.2483 | -60.0183 | 2025-09-03 05:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d0061b3-8a67-36e6-9d59-f3b31bf37262 | -8.88181 | -45.82245 | 2025-09-03 05:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed8b8343-9985-37fb-b030-0ea57dc8a928 | -12.49219 | -53.83512 | 2025-09-03 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 075d2663-9b89-37ae-aa19-d0c63b58cbd6 | -12.87555 | -48.03215 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b11ef28c-eb06-3817-9870-72635310a525 | -12.84641 | -48.02497 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31c48c23-46f5-37ca-a00e-f05a52212d0b | -15.09159 | -48.12838 | 2025-09-03 05:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84de4ddb-858e-32de-8de0-9954ad155b6b | -14.59826 | -54.5815 | 2025-09-03 05:14:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 408f01dc-6f01-3354-a28f-682e6a2186c7 | -6.78944 | -58.99659 | 2025-09-03 05:14:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56190e91-337c-3543-b47e-efe22e47545d | -12.98675 | -54.7544 | 2025-09-03 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c978ee68-bbc5-322a-a628-633bf8e58632 | -7.7637 | -61.20121 | 2025-09-03 05:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8709a37-d7a3-30ea-adae-e9aea2a747d6 | -11.85145 | -51.41838 | 2025-09-03 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4727c31-ba39-3893-b100-0d49d19f8c1e | -11.26827 | -48.9487 | 2025-09-03 05:14:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f09883fd-c71a-37e1-b68c-eb2c1df1267c | -11.85429 | -51.524 | 2025-09-03 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 514935e2-e620-3c12-a27c-fdf2724b942e | -11.6068 | -52.11764 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2ddfa365-501c-30fb-915b-f99f8ecbeb61 | -11.22072 | -55.06769 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1b4c268-f69b-3eda-b151-d60f54664009 | -8.85381 | -52.01588 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9158ec7-e6f9-3d79-b352-eeca8a2f5d43 | -11.63286 | -52.05918 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c5741d2-bcf2-32ad-b018-c068fe93c713 | -12.91839 | -56.92847 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a2be17e-b811-3529-84be-24ded5b523f0 | -14.06572 | -54.01236 | 2025-09-03 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 874e03f5-a1ca-330c-9306-0c30ce50f557 | -10.89615 | -45.7942 | 2025-09-03 05:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e2eba2c-f2c4-3ade-a1c0-6521500a44f9 | -11.6373 | -52.05978 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b9d0190-ac84-3dc2-a989-10d7e1f8b291 | -10.48154 | -53.63944 | 2025-09-03 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3eed96aa-d3ba-3ddf-a9c3-d9496b075a13 | -13.73961 | -46.93023 | 2025-09-03 05:14:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 13fed864-ebc8-3ee7-86d1-5e0bd9fb08ab | -12.94356 | -56.94799 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a9964ba6-d65d-37c4-a515-b5b9d5c64a41 | -11.92163 | -46.67275 | 2025-09-03 05:14:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f52cd8a3-0b26-306d-b8f6-d11e51fecf4d | -12.92672 | -48.08386 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bbc50120-0325-37b4-aa75-d1b26332579d | -8.30935 | -55.09626 | 2025-09-03 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8fe03fd5-7f66-3711-832f-259c849d0bd0 | -8.36559 | -48.30485 | 2025-09-03 05:14:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78f67b69-4485-3c4c-ab99-1a7270a09637 | -9.14361 | -49.64294 | 2025-09-03 05:14:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da952a68-e81c-3fea-a6bc-a4071840e404 | -9.9154 | -51.62185 | 2025-09-03 05:14:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4382bfed-e3c9-3664-a7ec-f295618c0614 | -11.9426 | -50.59813 | 2025-09-03 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c848db3-fdc9-3d40-aa36-572da400a1d3 | -11.41887 | -55.18739 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18314b2a-72cb-35a6-ae11-44c941c09412 | -11.44233 | -47.29773 | 2025-09-03 05:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c63a4b6-e5bf-35a7-a156-727b7f201387 | -9.99115 | -57.90718 | 2025-09-03 05:14:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46a42d0a-628e-3886-87b7-5a4c559e5dd3 | -10.45626 | -54.78129 | 2025-09-03 05:14:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26130e7c-75f5-308c-a0b4-3f465fc0b475 | -14.56851 | -54.53579 | 2025-09-03 05:14:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| efc31026-f5e7-3b1d-b9a8-1fcd64133a98 | -10.47439 | -53.63325 | 2025-09-03 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86b8b539-8a0f-3e22-9b82-0ed02115c603 | -13.81802 | -56.61122 | 2025-09-03 05:14:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 457d90cd-33d7-3087-b27d-401075e80acd | -12.51309 | -49.57169 | 2025-09-03 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d59e5477-cc12-3049-8531-6532e3b7a5ed | -14.81973 | -48.35162 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8aff74e4-119d-3989-a3fd-045082e794a2 | -12.91269 | -56.94309 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b13c5aa-81ec-372c-90ad-49deb3a038c8 | -14.34884 | -52.79733 | 2025-09-03 05:14:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22aa85b4-c9eb-36d9-8ba5-786f910f88b6 | -12.9287 | -56.95341 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c75ee571-8dd8-3626-896a-ea8a16d60ec4 | -12.29771 | -50.00637 | 2025-09-03 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b8bcf87-81d0-38b0-b0ba-18110e3b49a2 | -9.64093 | -47.85238 | 2025-09-03 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b36efedf-07c9-376d-8a49-0e3c20df3195 | -11.58354 | -52.12326 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 0565e6a2-7994-35d4-b168-270498bf269e | -14.58121 | -48.04997 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 32c8ade8-6b33-3336-9efc-8237f47b8c20 | -12.86384 | -48.02977 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8f02b976-8f37-3e09-a399-2083637556e0 | -13.09154 | -57.12056 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21230235-5cea-374e-a9c6-5eb4214a6643 | -11.65244 | -52.04846 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 65ee724b-0baa-34df-a3c8-54bbe2be072a | -11.6697 | -57.34661 | 2025-09-03 05:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9d9943e6-fc0a-3a3a-9270-da7d154ef79d | -12.97447 | -54.76429 | 2025-09-03 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 479d9b12-1204-3e0b-b6ab-0b2c52cf9515 | -11.60442 | -52.13498 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e3e72ef8-f094-3abf-a251-9b66d063e0c8 | -9.62731 | -47.04702 | 2025-09-03 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a43993b8-f170-3a5a-bce3-4df755764d3b | -10.14308 | -46.26216 | 2025-09-03 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d375a83-f235-3cde-80b1-19c93d6fcec5 | -11.6234 | -52.0623 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 526be8be-b564-3b84-8137-b44f5e813863 | -13.50624 | -47.02064 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c02bc71b-193a-31b4-8980-ab664c821e03 | -12.92363 | -57.01039 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7805c12c-dd3c-3484-8c03-1747858dbbba | -13.00114 | -48.09747 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d1997c83-c560-3960-ae56-bb7eba8e4ce2 | -12.88503 | -48.02936 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 261add24-cc8a-398d-92d7-6fe05b70295d | -12.9219 | -56.9986 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cff2e0a1-7941-3867-b39d-e128b44378f6 | -12.90982 | -56.93877 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3c864915-9e23-33cd-88d9-37893708c365 | -11.59531 | -52.10283 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a2d6b7b6-7f57-332f-b800-ced1c0f09620 | -9.76729 | -46.92268 | 2025-09-03 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 14887a4d-afce-3e7b-815c-60dfa16e7a89 | -8.06002 | -52.37127 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1d401bd7-8bad-3863-909a-5b5f15aea5fa | -6.77888 | -59.6428 | 2025-09-03 05:14:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ddab3328-7767-3030-9035-8874101d5996 | -13.45782 | -46.93363 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b8668a23-6cc7-3012-9c9e-c93e33be9033 | -12.94414 | -56.96741 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c8987a3-8593-3315-864a-2fa1b61ab576 | -12.63738 | -56.99018 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9f70356-b5b3-36e4-8a41-c257c6104c13 | -12.52634 | -53.82388 | 2025-09-03 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e954b13-a5bf-3272-a7a2-48a8070f98e6 | -15.01491 | -50.06424 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0d154d5-73cc-3961-a838-738c805933bd | -11.03671 | -45.0701 | 2025-09-03 05:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c23d972e-7079-3fc0-bc7a-37f084803916 | -6.83818 | -59.36444 | 2025-09-03 05:14:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 76521aa0-3e95-3cae-acc4-91bf91138f49 | -10.27981 | -46.49812 | 2025-09-03 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f99be9a-0d0b-3227-bafe-67afb0b15b28 | -9.13777 | -49.64806 | 2025-09-03 05:14:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 171010aa-e3ce-3ec9-b7c8-20b1d2d5b38d | -8.08907 | -47.5961 | 2025-09-03 05:14:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 095af902-a853-3480-846f-f72fee7a890c | -11.06402 | -52.07278 | 2025-09-03 05:14:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d819e99c-7866-3262-bc11-9515c5b3938d | -11.41855 | -55.19066 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d37b338-6b72-3b89-8db8-bff1f9fec555 | -11.03735 | -45.06188 | 2025-09-03 05:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5916a202-9f48-382c-a90b-f8246e9707b5 | -12.92719 | -48.0798 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a284a455-014c-3775-93f7-bae7f1231b9c | -12.90726 | -48.09713 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b7608ab-f973-35c6-b8aa-7774f26cc571 | -11.60179 | -52.12136 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 98c2e9a0-cdbc-367c-b25b-8221ad6fa3ac | -9.75078 | -46.91097 | 2025-09-03 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b175fd0-1009-3a5f-994c-c493db04ad0c | -11.60512 | -52.06387 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd289ae7-24be-3c2b-b520-eaad35a55d80 | -11.94753 | -50.59879 | 2025-09-03 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0959c63-92d0-329f-9ca7-08f43626757e | -11.6516 | -52.04609 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 499a641e-367a-32d0-b2bc-ea36888b6fae | -8.89089 | -45.80244 | 2025-09-03 05:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7b46a4d1-f84c-38a0-a5cb-d02561624128 | -9.63807 | -47.86369 | 2025-09-03 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4c431b7e-a993-3093-9d0a-fed0e7386176 | -10.9728 | -50.91548 | 2025-09-03 05:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c95308e-d4fe-380f-a380-b5be4b28080d | -11.57073 | -49.90888 | 2025-09-03 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae917fb1-a031-3712-9759-25719afc5b89 | -8.86119 | -52.02512 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47a2a76d-474b-3a5d-93b8-f562124f6d75 | -8.35968 | -48.30743 | 2025-09-03 05:14:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| edf88b7c-9954-37ce-9430-0f1a24bdcc4a | -7.77879 | -50.9697 | 2025-09-03 05:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64bf8196-df70-3b6d-806e-76c657e880b2 | -9.7624 | -46.91734 | 2025-09-03 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1b505ee-66b6-36fa-ba8e-99ac84815436 | -12.83709 | -48.05345 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f675a06d-0fdf-37ea-8f6d-1ed9eb3fae80 | -6.44195 | -58.1406 | 2025-09-03 05:14:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d14da62-ab0e-3291-acd1-dabb7db26eb0 | -6.67808 | -58.86284 | 2025-09-03 05:14:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README89.md)

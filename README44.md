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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9336f43b-8e38-3a7a-be13-4072269f314b | -14.40832 | -51.25807 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8ed06225-91b4-3bac-b1c0-cba417395f3c | -19.23516 | -42.94365 | 2026-10-01 04:17:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0f62fbb3-0dd0-39c5-a673-8a30a4ff90f3 | -13.37563 | -46.8367 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b7d8644-0ec4-3ad6-b55a-68b67f6827df | -12.18673 | -47.38788 | 2026-10-01 04:17:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cea2e110-02f7-3d01-8e4d-e994b12e69fc | -13.66491 | -53.94767 | 2026-10-01 04:17:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0074f29b-baa9-3d57-b903-e8fa47c6448f | -16.90159 | -42.10632 | 2026-10-01 04:17:00 | NPP-375D | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 98da32ae-e7cc-3d30-9c13-6b0cf256392a | -13.38674 | -44.02181 | 2026-10-01 04:17:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46ec634d-bc76-3b9f-838e-940ce8d412b8 | -12.18545 | -48.43364 | 2026-10-01 04:17:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 5476fec8-046f-3827-9681-8146a0b4d7ab | -13.10821 | -51.22257 | 2026-10-01 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a231a185-ad55-38a9-ace7-5459c7cacf90 | -13.86076 | -44.4418 | 2026-10-01 04:17:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13fc308f-8659-3b86-a27e-e9ebfe43853e | -15.23559 | -46.14987 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c4f33edb-65e2-3088-a74a-f4af9953266e | -14.15077 | -51.11908 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b419ec5c-0972-3cbb-8a5d-01c2bac4a4aa | -15.30592 | -42.77728 | 2026-10-01 04:17:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ed448ce-61db-3ba3-9c7c-ee6ee21b2cac | -17.88358 | -44.31015 | 2026-10-01 04:17:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 403277ea-0d1b-3525-8b42-999e8499f78f | -14.14499 | -46.24631 | 2026-10-01 04:17:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5afdc43e-d6e7-340c-ad0d-f3cff90e3534 | -14.49066 | -48.30426 | 2026-10-01 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0df3ce4e-993b-3343-bec5-59fe35d58aaa | -13.10169 | -51.19823 | 2026-10-01 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8aaa44b3-8736-328b-9766-c9dd4d44a8f4 | -14.86677 | -51.85474 | 2026-10-01 04:17:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 3379629b-8b62-3788-96c9-5edcde97d638 | -14.73744 | -47.13544 | 2026-10-01 04:17:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 564d69ce-32b0-33f7-8d60-0352f6312c11 | -14.361 | -44.77435 | 2026-10-01 04:17:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4bb08947-fb9f-3add-a41b-fbe694cd4a84 | -18.09743 | -44.41223 | 2026-10-01 04:17:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ec6584b-de2f-3dcd-a59d-d639e9ca9506 | -13.53762 | -49.16731 | 2026-10-01 04:17:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8c8d0894-512f-354b-8215-8b3dfddcd5f5 | -13.38885 | -46.82371 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| be03841c-ccc7-3f47-9d75-f9946642b782 | -14.87227 | -51.85596 | 2026-10-01 04:17:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f7875aee-a680-3653-a2e4-34b959ea3955 | -13.51161 | -46.88515 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8406fba1-e62f-3743-b52f-db9126cc0742 | -16.13962 | -43.74054 | 2026-10-01 04:17:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1a753bd1-b7cb-3ae1-9a11-de3121e02787 | -15.22837 | -46.13535 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 671933c2-0366-3031-ac18-69644628735c | -13.38608 | -46.81579 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d91b5b6b-0a82-3553-a27b-8d1494754300 | -14.14201 | -46.24055 | 2026-10-01 04:17:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d6c38740-cb05-33c6-a2eb-7b576e6133fa | -14.38115 | -51.29944 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8fd63cda-9105-3f87-932d-fc774a80bc84 | -13.88785 | -44.455 | 2026-10-01 04:17:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 92a854e6-ce7e-3465-8f04-5ab719d8c111 | -14.40015 | -51.27076 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| a49b5c6b-89ff-36f1-bb62-cc4a6a28e9ec | -14.15609 | -51.12023 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07cffe6b-9096-3cfa-a521-c32948d01c8e | -11.7449 | -50.40705 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e05eea24-dd44-3253-9385-f5c2310b689e | -22.08632 | -46.97706 | 2026-10-01 04:19:00 | NPP-375D | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d4a5470-0d89-3a14-b348-28b80d22d98b | -20.90115 | -47.41262 | 2026-10-01 04:19:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 693523b5-cbeb-3199-98f3-d90395284103 | -21.49579 | -46.61426 | 2026-10-01 04:19:00 | NPP-375D | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 2971ab16-8b85-33c7-90f3-5bb9ff9f0a31 | -20.86118 | -47.10221 | 2026-10-01 04:19:00 | NPP-375D | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e97c5d5-37e2-3e9f-8552-0f347f4e20f7 | -20.18517 | -47.40447 | 2026-10-01 04:19:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 12.5 |
| e9231bf9-eed6-367a-b75c-3cc732a6d015 | -20.53777 | -45.76646 | 2026-10-01 04:19:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ddfba14d-aa3b-326b-922c-32bfb256af33 | -21.71551 | -47.14147 | 2026-10-01 04:19:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1f3b7695-f992-3c8d-b949-cc301afc3fc2 | -21.71352 | -47.13152 | 2026-10-01 04:19:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb18e22d-25b8-3b2c-9e85-2bca163e237f | -22.14453 | -46.67274 | 2026-10-01 04:19:00 | NPP-375D | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 599ba2eb-ab9f-3981-b252-cffb6354ed2f | -20.90023 | -47.41758 | 2026-10-01 04:19:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 659affbf-6acd-340a-b81c-ff30b283d8b8 | -21.17625 | -47.01477 | 2026-10-01 04:19:00 | NPP-375D | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| abe6ed56-2cd9-3086-b3cd-0830197aea58 | -22.18924 | -46.9269 | 2026-10-01 04:19:00 | NPP-375D | ESTIVA GERBI | SÃO PAULO | Brasil | 3557303 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 156f58ce-ab58-329a-94fe-8223456e03e3 | -20.18897 | -47.40522 | 2026-10-01 04:19:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c1472453-9ee1-3aa8-bda6-55d45fa5e835 | -20.89647 | -47.41682 | 2026-10-01 04:19:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 224373c4-17c2-3216-9716-b743460974a0 | -22.14376 | -46.67707 | 2026-10-01 04:19:00 | NPP-375D | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 42b9452a-aaae-35de-b6b0-5af401c35c2a | -20.18859 | -50.89861 | 2026-10-01 04:19:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1b48ca14-b3e4-3d40-a522-f11298b622e8 | -21.05754 | -47.03858 | 2026-10-01 04:19:00 | NPP-375D | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 639707c8-14e6-3e83-8bef-5580e94078f1 | -21.06004 | -47.0366 | 2026-10-01 04:19:00 | NPP-375D | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6844ed79-fab9-3497-b6e2-cf23b2ab2e88 | -20.7516 | -48.58377 | 2026-10-01 04:19:00 | NPP-375D | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9fbf4a08-b91a-3b5f-9ccd-0156c9b82f46 | -21.47855 | -46.5654 | 2026-10-01 04:19:00 | NPP-375D | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 335b48ec-c0d5-345f-8a78-2864b75cc52f | -22.14018 | -46.67635 | 2026-10-01 04:19:00 | NPP-375D | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| b394925c-b43c-3f87-aa8c-ee4926daffb5 | -20.47769 | -50.91035 | 2026-10-01 04:19:00 | NPP-375D | APARECIDA D'OESTE | SÃO PAULO | Brasil | 3502606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 956046cb-e7fd-3a2d-a458-05ed8c43afda | -22.61122 | -44.76947 | 2026-10-01 04:19:00 | NPP-375D | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f62ba2f7-4929-3529-ba89-cb6356749cf2 | -20.5385 | -45.7623 | 2026-10-01 04:19:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be3d6407-a909-3c11-a1bb-c98930c72d72 | -20.89738 | -47.41193 | 2026-10-01 04:19:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 05340c5c-18fc-3b8b-9a29-198923651c50 | -20.18894 | -50.89997 | 2026-10-01 04:19:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d87b1e62-4126-3971-8e99-af07384dfcee | -21.46096 | -48.67844 | 2026-10-01 04:19:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86ee91ed-e584-3ecd-984d-25626c699788 | -3.1839 | -54.0839 | 2026-10-01 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| ca7262e3-c4d9-39ee-ae8c-ee1b8c6e4f64 | -11.7906 | -50.5236 | 2026-10-01 04:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| d94a7dd5-2ae8-348d-b1f2-238696fad96a | -3.295 | -53.8597 | 2026-10-01 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 7dda066a-022f-3769-9146-efffde6f67b6 | -3.1838 | -54.104 | 2026-10-01 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 1735cd47-12e2-3478-a55c-9fff88b9a28c | -3.1655 | -54.0844 | 2026-10-01 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 129.1 |
| 7317a92b-6ff5-3101-b5ed-85b89a767033 | -11.791 | -50.5021 | 2026-10-01 04:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 7f0cd532-18bd-3caf-9f8f-98293fbf7a4e | -3.2766 | -53.8602 | 2026-10-01 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| e8ef09cb-cada-3362-8e22-079cceb4c67e | -3.1655 | -54.1045 | 2026-10-01 04:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| aa71407e-a704-366c-8fcb-e8e896861c7a | -12.1857 | -48.4345 | 2026-10-01 04:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 5cf7e589-fab4-3c53-bfe6-ab64408bac8a | -13.6479 | -53.9336 | 2026-10-01 04:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 49419557-b9c1-35d8-82c8-f3c095e5006c | -3.2951 | -53.8395 | 2026-10-01 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 8306c19b-ba68-3e39-b155-268bcbe76286 | 1.64739 | -50.9067 | 2026-10-01 04:29:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06d270bc-d36c-3aaf-ad89-091839f79bf3 | 2.16703 | -50.92184 | 2026-10-01 04:29:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98167487-9cbf-34f5-8304-0dcf5e01d3f7 | 1.96905 | -50.86163 | 2026-10-01 04:29:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cce66544-c4db-3e3c-b541-f77cdbcc58b8 | 1.96644 | -50.84464 | 2026-10-01 04:29:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a03e1f69-e25d-32d6-b790-bf9d34863178 | 1.98203 | -50.82919 | 2026-10-01 04:29:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 700f63bc-05c1-3444-bf41-7ae2549b76a4 | 1.97083 | -50.84396 | 2026-10-01 04:29:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b48cd2c0-b485-370f-afab-495e7a61ec1a | 1.97392 | -50.8348 | 2026-10-01 04:29:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b02545b-d95e-3266-a876-97a3bf9815a1 | 1.97457 | -50.83904 | 2026-10-01 04:29:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4672e77d-92b4-3f0d-8043-6b177d767621 | 1.98531 | -50.8504 | 2026-10-01 04:29:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 928cf877-da44-33ba-aa23-73923b908115 | 1.96465 | -50.86232 | 2026-10-01 04:29:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 617defba-d410-390f-8037-cb057f1b3a62 | 1.97018 | -50.83972 | 2026-10-01 04:29:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6262208c-235b-38ff-b10f-abdf7c922a21 | 1.98269 | -50.83344 | 2026-10-01 04:29:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec04b85f-a986-33d3-8080-5f8aa30eb15a | 1.96774 | -50.85313 | 2026-10-01 04:29:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e933b78-bb97-3e6e-a8f8-db1f2323d449 | 2.48508 | -50.79483 | 2026-10-01 04:29:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1242e40a-e20b-310f-a844-f7dce970c540 | 1.96531 | -50.86657 | 2026-10-01 04:29:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72d6b61a-2de1-33a9-b7ee-18e0012be43e | 3.44333 | -51.27388 | 2026-10-01 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 180b0c4c-1e0c-364c-a971-4af8c5dea314 | 1.98158 | -50.85533 | 2026-10-01 04:29:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| adeafed2-dc08-3b1f-b0d4-00bc90df69af | 1.9783 | -50.83412 | 2026-10-01 04:29:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ddd2f68-35bb-3532-94da-d6b9dc9b6acf | -13.6671 | -53.9314 | 2026-10-01 04:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 669642c4-e01b-34cf-90c7-3ce6e85f3fb2 | -13.6479 | -53.9336 | 2026-10-01 04:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 0f7042f3-2a56-3271-8a54-65de75bb0cb5 | -3.18804 | -48.0238 | 2026-10-01 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c9d6404-4ab0-3453-80e0-d4fd796511ce | -2.91365 | -51.31261 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| daa1cbbb-7af0-3344-bc5f-bb750d46e960 | -4.25486 | -50.75744 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 89b9b18b-bdd5-3cd4-93f6-79067966821e | -4.29471 | -50.80256 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5d8d47d8-b6da-3935-bd1c-ac7978336d1d | -4.30318 | -50.75132 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 582d3b26-918d-3a5f-9007-ff80d1935a24 | -3.01035 | -51.46371 | 2026-10-01 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c2716ee4-e9f1-30a8-b7eb-0ba4acda6cb7 | -3.15841 | -54.0968 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f7c4b06-eed6-315d-acd1-507824e6252e | -2.97115 | -51.03908 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README45.md)

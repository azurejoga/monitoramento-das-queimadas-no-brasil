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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 494380d3-cb0d-3abe-98dc-15b2cd85a15d | -10.21187 | -48.07761 | 2025-12-24 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e62cffe8-94b4-3370-a74f-dff56a3bbd9f | -7.23471 | -43.08692 | 2025-12-24 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c958afad-e86c-334a-ae49-648c1fbccd2a | -7.82647 | -42.9421 | 2025-12-24 04:46:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1130c21e-0e46-3879-b413-8ebcc410a4aa | -10.21242 | -48.07987 | 2025-12-24 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 307aa87b-f009-3e39-8966-3deb29f1f5be | -11.83299 | -43.79117 | 2025-12-24 04:46:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 199caf96-fcaf-30a5-a792-cbb421797f2f | -13.20957 | -53.32927 | 2025-12-24 04:48:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d99bb9ee-49e6-328d-a4d2-65f6329d3d42 | -15.92013 | -43.72566 | 2025-12-24 04:48:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4efeef7e-33cb-3dbe-9118-56f63efa26bc | -12.59888 | -48.76972 | 2025-12-24 04:48:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd23ce3d-e453-33b7-836e-d2fe006e23a5 | -16.61018 | -54.46972 | 2025-12-24 04:48:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8ce5992-ed17-3267-ba41-a70c8da01f51 | -13.87696 | -49.43797 | 2025-12-24 04:48:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a540276-d1f2-39b0-a571-feafcf1997be | -16.3202 | -53.79227 | 2025-12-24 04:48:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e105777c-8927-37f5-a0c4-2345ebd67f3e | -16.30383 | -45.10187 | 2025-12-24 04:48:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7522ded2-6533-3873-abb4-1ee34e6c57f5 | -12.59954 | -48.76521 | 2025-12-24 04:48:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0558cad6-725c-31cf-95c1-bd9217c1d9f4 | -16.30768 | -45.10261 | 2025-12-24 04:48:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc268bd1-b8c2-32b8-b9d4-a20ddde537a5 | -17.58443 | -46.66704 | 2025-12-24 04:48:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb90f2c3-e9d0-3a4d-9b58-7f9f7edaff56 | -16.19814 | -47.60295 | 2025-12-24 04:48:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ab7709d-b6e1-370a-a401-1eb9b882ce8f | -15.92222 | -43.72644 | 2025-12-24 04:48:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 361d8511-dbc3-34b7-8c27-0cbaf706150b | -14.04299 | -50.53245 | 2025-12-24 04:48:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f173cb27-6ce7-3367-b7df-8a820fe5ad84 | -16.32351 | -53.79284 | 2025-12-24 04:48:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8f318f1-de5f-39d2-a28c-3e3f05d56cd6 | -16.31632 | -53.7953 | 2025-12-24 04:48:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6447e95e-e5bf-3913-8c1e-48e912043ad3 | -16.58861 | -45.87879 | 2025-12-24 04:48:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8e0e02b-9044-3ea7-a129-6602437e2b18 | -14.03604 | -50.53137 | 2025-12-24 04:48:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1036d2db-2835-3905-b7fa-d696c8fb8b53 | -16.19866 | -47.59892 | 2025-12-24 04:48:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ecddf4b-c5f2-35a4-bf9b-71abde04f3ff | -17.57989 | -46.66637 | 2025-12-24 04:48:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bd61a9dd-9fbc-34d0-9178-1be4083e97f7 | -13.29704 | -49.23536 | 2025-12-24 04:48:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e83823a-918c-33dd-bc32-32d70a1c19bb | -16.81911 | -51.98045 | 2025-12-24 04:48:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ff9298b-b55c-3245-bd49-16307697ac0d | -16.31688 | -53.79172 | 2025-12-24 04:48:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3833f173-8e87-322c-9ac1-6ee700bd5093 | -17.57932 | -46.67112 | 2025-12-24 04:48:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1bbaaf53-cdfd-340d-b14b-fc88b7c77149 | -13.20625 | -53.32872 | 2025-12-24 04:48:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07663233-6efc-329b-a047-7acb035465c5 | -12.60102 | -48.7682 | 2025-12-24 04:48:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2260ff6-4457-3314-a3a4-8c6d547d7166 | -14.03952 | -50.53191 | 2025-12-24 04:48:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9689aca8-dd07-39db-bb93-5c2f98c7a881 | -14.03894 | -50.53584 | 2025-12-24 04:48:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b5aafeb-bf8d-3c30-b975-022d9ce4967e | -16.18438 | -43.72618 | 2025-12-24 04:48:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 745c1ca2-097e-317a-943a-088e9063b138 | -3.5573 | -41.6357 | 2025-12-24 04:50:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 79.6 |
| b664f8be-b6e9-382e-a31c-457e4706f96e | -20.9186 | -48.66886 | 2025-12-24 04:50:00 | NOAA-21 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4560b1de-5529-3ff7-8306-0fd67793ab0d | -20.62759 | -48.93967 | 2025-12-24 04:50:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9b43efdc-4655-3b52-97ad-da870c312223 | -19.6983 | -47.96701 | 2025-12-24 04:50:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b07d4139-7f6f-360e-b6a5-c467d7becf89 | -20.91616 | -48.66376 | 2025-12-24 04:50:00 | NOAA-21 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b012a856-1574-3c16-912a-6a183488bf58 | -17.91637 | -54.13096 | 2025-12-24 04:50:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4fe1a598-8866-35d9-a09f-5d3b354b23d2 | -17.91694 | -54.12734 | 2025-12-24 04:50:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bef07e0d-d552-34d5-8a15-3f161b84440e | -20.91569 | -48.66771 | 2025-12-24 04:50:00 | NOAA-21 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 06f9914d-596e-3119-9447-4287ef24b03c | -20.99759 | -48.76117 | 2025-12-24 04:50:00 | NOAA-21 | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 1fe87953-3b16-37fc-ad7e-338026dc6248 | -20.95805 | -47.18153 | 2025-12-24 04:50:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 026d0198-6e77-36f4-aae0-0826ca2cb3f7 | -19.21082 | -53.43634 | 2025-12-24 04:50:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| abd96636-c693-37e0-b227-07b2d73c0303 | -21.05526 | -48.43026 | 2025-12-24 04:50:00 | NOAA-21 | TAQUARAL | SÃO PAULO | Brasil | 3553658 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73d640e3-70fc-39ff-bff0-fd04d6712495 | -20.6235 | -48.93911 | 2025-12-24 04:50:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 536b882e-0cb8-369c-b527-9a746520f9a2 | -20.91442 | -48.66829 | 2025-12-24 04:50:00 | NOAA-21 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 058caff0-ce31-3296-b259-b16f5004d19e | -20.91491 | -48.66434 | 2025-12-24 04:50:00 | NOAA-21 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9ab33b50-0252-35f1-add6-38c5d299c7ea | -19.69401 | -47.96643 | 2025-12-24 04:50:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 70839310-df65-3fb7-82e2-0fff7f19c90f | -20.99809 | -48.75714 | 2025-12-24 04:50:00 | NOAA-21 | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 3ab8a8db-6fca-38b1-be95-01548bca1c12 | -22.39006 | -49.89312 | 2025-12-24 04:50:00 | NOAA-21 | OCAUÇU | SÃO PAULO | Brasil | 3533700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e24b6d49-b5d8-3b18-a139-ac42c17c52e3 | -17.9158 | -54.13458 | 2025-12-24 04:50:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d826f578-e0fb-3450-b26f-fee13265f970 | -17.91522 | -54.1382 | 2025-12-24 04:50:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 874a67d8-e45e-3ec0-82b8-79e73097e668 | -25.51567 | -49.46697 | 2025-12-24 04:53:00 | NOAA-21 | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6eac996c-c4c4-3872-b56d-888116810626 | -25.25539 | -51.03008 | 2025-12-24 04:53:00 | NOAA-21 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 47d13e6d-047e-31c1-bf5e-ee0709efa89f | -25.25434 | -51.02564 | 2025-12-24 04:53:00 | NOAA-21 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 90813bea-f043-3d74-9311-347ba7c394fd | -25.25817 | -51.02624 | 2025-12-24 04:53:00 | NOAA-21 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 553a5150-6a97-336e-858f-b5f710174dac | -3.5386 | -41.6367 | 2025-12-24 05:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 65.5 |
| 59ca88aa-0c67-3086-a949-a7cf7424894d | 4.35559 | -60.33875 | 2025-12-24 05:12:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c57e434a-b544-38c3-83a7-376a7368936c | 4.35969 | -60.33805 | 2025-12-24 05:12:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 41ff3e97-4838-37d8-bd87-1773758a405a | 3.67786 | -60.29665 | 2025-12-24 05:14:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99f450ae-618e-3401-8e5a-3e4ebe637d74 | 3.64556 | -60.27208 | 2025-12-24 05:14:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e3d517a-cb38-3771-8ab8-906efade8db4 | 3.64501 | -60.26854 | 2025-12-24 05:14:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e81e831c-294b-36b8-8829-ffdcaa1a10e5 | -17.91331 | -54.13322 | 2025-12-24 05:18:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3da40fb6-7ed7-3dde-9fff-e2ba28baccc0 | -16.31409 | -53.79333 | 2025-12-24 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 68c0e23b-6078-3c6e-917b-24b43e2ee77a | -16.31653 | -53.79169 | 2025-12-24 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f1a4475-b2d9-3782-a751-ec599185d294 | -14.03965 | -50.53049 | 2025-12-24 05:18:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3026b2c1-29c0-32f8-a4b3-4e18acd8bbcf | -13.20777 | -53.32667 | 2025-12-24 05:18:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bbb9abd-72d6-3b83-88cf-5df8b70593a6 | -16.32261 | -53.79472 | 2025-12-24 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a33e197a-98df-3ea2-95ae-964a32329752 | -14.03926 | -50.53364 | 2025-12-24 05:18:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c5d71225-3465-352d-8da6-89739ba1c619 | -16.32079 | -53.79242 | 2025-12-24 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 22ecd99f-aa1a-3385-b312-d54f96fcd7f2 | -16.32317 | -53.7905 | 2025-12-24 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e9d9459-741d-37ef-97ec-c1be00142f3c | -16.316 | -53.79588 | 2025-12-24 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c4a23e7-c378-3859-91d4-be383ae00a8f | -16.31834 | -53.79407 | 2025-12-24 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f5a674c1-2b71-34c3-8987-eefe3b215e36 | -17.91279 | -54.13741 | 2025-12-24 05:18:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c0cf323-b725-3fa3-bf0b-76727816115a | -20.99179 | -48.76118 | 2025-12-24 05:20:00 | NPP-375D | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 72748e05-7b43-3221-a529-9e2060232de6 | -20.99595 | -48.75658 | 2025-12-24 05:20:00 | NPP-375D | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4f86262d-a492-3d67-87cb-f82fecedf813 | -22.36039 | -47.03854 | 2025-12-24 05:20:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 95527be1-fc2b-3aed-afdc-b2765572964e | -20.9955 | -48.76189 | 2025-12-24 05:20:00 | NPP-375D | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8ad9d8c2-b869-3dc1-a75d-109baf215e3c | -20.91468 | -48.67087 | 2025-12-24 05:20:00 | NPP-375D | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8cca3793-aa11-3836-8ec7-6d9ec58b6984 | -20.91514 | -48.66585 | 2025-12-24 05:20:00 | NPP-375D | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 28736b1d-3ba7-3dc3-a7b3-134f26600d09 | -22.362 | -47.03988 | 2025-12-24 05:20:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 078bab2b-4f4d-3100-b87f-085f1a459d42 | -22.36247 | -47.03334 | 2025-12-24 05:20:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a5ec268-9d93-37cc-beea-cd40e033fd50 | -22.35497 | -47.03949 | 2025-12-24 05:20:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6be87f3e-f78b-37f9-a8ea-8588fa23c7ef | -20.62405 | -48.94152 | 2025-12-24 05:20:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 60dd216a-baa1-3015-9f33-7c2172d5cebd | -20.99807 | -48.76178 | 2025-12-24 05:20:00 | NPP-375D | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| bc0a72c6-f4d4-31cd-847f-e8bff254065e | -22.35546 | -47.03267 | 2025-12-24 05:20:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a58beb9-7f87-3e83-817b-665be1d1d911 | -3.5573 | -41.6357 | 2025-12-24 05:30:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 85.3 |
| f998eeea-6db7-3a82-aa40-17748ea4a214 | 4.35533 | -60.34085 | 2025-12-24 05:33:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 14e83714-e604-37e3-9777-71a92c29ba58 | 3.64624 | -60.26653 | 2025-12-24 05:33:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff9a2ec7-68a5-380e-91f2-e72879e5f8ea | 4.35477 | -60.33736 | 2025-12-24 05:33:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 44ab078e-3adb-3356-b72e-165809464ed4 | -14.62015 | -55.52599 | 2025-12-24 05:37:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92b4b06b-fd4d-3977-8fce-f736e62d6f95 | -16.31947 | -53.7967 | 2025-12-24 05:40:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f486e694-acce-3178-8a72-0c3c6007ba36 | -16.31307 | -53.79553 | 2025-12-24 05:40:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bd011bb-109c-3f19-bc85-44a4ea72bdf0 | -3.5386 | -41.6367 | 2025-12-24 07:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| e1918183-0457-388d-bf04-840addfed838 | -3.5573 | -41.6357 | 2025-12-24 07:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 66.0 |
| 444952d9-5922-34c9-b65a-3b30af025e93 | -3.5573 | -41.6357 | 2025-12-24 07:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 73.4 |
| da2ccc2b-4a3e-34bf-99b4-6792b4fd3906 | -3.5386 | -41.6367 | 2025-12-24 07:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 76.5 |
| 5722f625-2c9f-3be4-b557-6650fc4b6bbe | -3.5386 | -41.6367 | 2025-12-24 07:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 80.9 |
| fe7195f0-8d24-3717-8478-0f648a8693cb | -3.5573 | -41.6357 | 2025-12-24 07:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 83.8 |


[Clique aqui para ver as próximas entradas](README5.md)

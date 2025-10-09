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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c199196a-c089-3cb4-91d6-8f795dcd524d | -15.3988 | -47.9712 | 2025-10-09 13:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 7f1991b8-450a-3b98-8a4e-2a7de91569d1 | -8.1618 | -43.323 | 2025-10-09 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 109.0 |
| 8bfe21e7-eb6f-36f2-a551-a685c41e14af | -12.425 | -45.7056 | 2025-10-09 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 222.5 |
| 05d69f9d-4a91-3afa-b8dd-048ba37b449f | -11.993 | -45.1958 | 2025-10-09 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 154.2 |
| cb6e0486-ce73-3d85-b3eb-c4b4c13d161b | -13.2779 | -48.4607 | 2025-10-09 13:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 118.9 |
| e4299cd7-5cb7-3261-bdda-3abbded23a77 | -15.2384 | -46.3616 | 2025-10-09 13:20:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 92.0 |
| abfcbf94-7f62-3546-8f9d-87a6d2134ea2 | -8.1993 | -43.3424 | 2025-10-09 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 265.9 |
| 60dc9ee1-8ce2-31b7-8a30-10b36c43eef2 | -11.7829 | -45.1578 | 2025-10-09 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 83abf30e-bc42-360a-bd1e-014b92884b35 | -11.48 | -44.9711 | 2025-10-09 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 125.5 |
| f81596ed-bb58-3dcd-b982-f96bb35144c2 | -11.7215 | -44.3084 | 2025-10-09 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 192cd77a-7b27-37c0-841e-0b5a6bee25ca | -13.0586 | -47.8262 | 2025-10-09 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 629bdd70-0b3c-30a5-9964-2ec5e8ce8b5c | -8.8335 | -45.3741 | 2025-10-09 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 301be8b6-fb52-3d7e-b65c-066dedfdd522 | -15.2384 | -46.3616 | 2025-10-09 13:30:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 84.1 |
| d2c8c03e-0d74-3490-98ba-247186f8c0ad | -15.3984 | -47.9938 | 2025-10-09 13:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 9f7d1285-153e-3003-8dfd-54994da8aaab | -11.743 | -46.3513 | 2025-10-09 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 186.4 |
| d8f72023-37b8-3269-842c-b2b112100b3a | -8.0863 | -44.8139 | 2025-10-09 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| d1cfa695-827c-392a-a9c5-9b33d8dc15d7 | -14.2559 | -45.8681 | 2025-10-09 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 84b48231-924e-3ba6-8c24-9f6d3e930801 | -12.6968 | -47.6552 | 2025-10-09 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 140.6 |
| c2de46f7-fdae-3334-a0c0-afff24f926d1 | -8.1052 | -44.812 | 2025-10-09 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 264bf862-2a15-3c1b-a031-2630ce989d16 | -10.2092 | -44.5678 | 2025-10-09 13:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 249.4 |
| ca942805-915e-3799-afc8-d1d7a32b2db6 | -8.1807 | -43.321 | 2025-10-09 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 205.1 |
| e2567f43-db2b-3326-b4d6-8a515d7c128e | -10.1905 | -44.5471 | 2025-10-09 13:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 163.4 |
| da74154b-28c2-3287-b629-912bc055c205 | -15.5554 | -45.3278 | 2025-10-09 13:30:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 20852c79-7522-366a-9538-5987013aafd6 | -18.0589 | -44.9632 | 2025-10-09 13:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 104.3 |
| dd5a6373-bf2c-3f71-aa59-e26d253e7037 | -15.3988 | -47.9712 | 2025-10-09 13:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 5b448e5d-fe77-3aa3-bb2f-470bf5f74b0a | -15.556 | -45.3043 | 2025-10-09 13:30:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 1e3c4c93-b83c-3298-b24e-309434d3f00d | -13.2971 | -48.4579 | 2025-10-09 13:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 57c54f56-6b36-39b7-8099-fbe5c2b7ed6d | -8.1618 | -43.323 | 2025-10-09 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.9 |
| d67cffbc-bccd-3b6b-a3bd-f5ac960cb6df | -11.7833 | -45.1347 | 2025-10-09 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 132.4 |
| e8fb1e18-21df-3dbf-8684-fcdbd965640a | -11.4992 | -44.9684 | 2025-10-09 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 37f6c88c-29a6-3b87-bc12-6d580e11ec9e | -8.1804 | -43.3445 | 2025-10-09 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 158.4 |
| 1cf42af3-ed0a-3e98-a7db-ef293acdf812 | -13.7548 | -45.723 | 2025-10-09 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 6af18616-c5db-34ff-9712-d44e95fe29f6 | -10.2095 | -44.5446 | 2025-10-09 13:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 125.0 |
| dd4c9f3e-e331-3e90-8bb1-1cb5fef49a6c | -11.993 | -45.1958 | 2025-10-09 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 163.6 |
| 9a075175-0901-3c90-ae53-d7a5226635b0 | -12.6964 | -47.6776 | 2025-10-09 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 191.3 |
| 6c283416-3c57-36f1-96b1-1b41d9b5c6eb | -16.2788 | -47.1556 | 2025-10-09 13:30:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 86.6 |
| eda1b299-539b-3696-9a59-d624754a9152 | -7.9963 | -44.4788 | 2025-10-09 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| c6551864-ac54-33e8-9080-bb83ef4b1ef9 | -8.6106 | -45.102 | 2025-10-09 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 8749286c-ad72-32e4-840d-37010dfe1db0 | -9.3209 | -45.6607 | 2025-10-09 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 46c841f3-bcea-3283-837c-abd4d961e594 | -15.4772 | -47.9578 | 2025-10-09 13:30:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 9ae43b36-2008-3565-8781-4ea8491151c3 | -8.199 | -43.3659 | 2025-10-09 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| 448e66d6-a709-3f1c-8447-9c2fe20a6b22 | -14.2754 | -45.8647 | 2025-10-09 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 145.6 |
| c8d5f916-d89c-39cf-a2d7-a9f866288512 | -15.018 | -47.5401 | 2025-10-09 13:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 5f9db49d-e669-3c07-ab03-21557abc2291 | -8.1993 | -43.3424 | 2025-10-09 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 223.1 |
| cd54cc16-cac6-34ac-bb55-b13d493b59e8 | -10.9109 | -47.1129 | 2025-10-09 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 127.2 |
| c9f6ef8d-71ff-3d4c-9374-35da69ba334d | -12.425 | -45.7056 | 2025-10-09 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 9227094d-ad42-3847-bfaa-0091eaa5fbac | -10.1901 | -44.5703 | 2025-10-09 13:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 214.1 |
| b5b13507-3a9f-3f81-8b5d-d57caf1d5ecb | -13.2967 | -48.4801 | 2025-10-09 13:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 118.0 |
| dcfd519d-ca37-3e66-9950-4bf706b45e3d | -11.7238 | -46.354 | 2025-10-09 13:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 166.5 |
| 0489e156-904b-3fcb-b45a-2e7934f33927 | -14.2754 | -45.8647 | 2025-10-09 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 163.9 |
| f67dbc0a-5208-33e0-99d9-9c51366b57b2 | -8.8335 | -45.3741 | 2025-10-09 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 123.8 |
| b415a3e1-4ccc-32dc-aa97-7244c7b8c582 | -13.1361 | -47.7926 | 2025-10-09 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 26803b1b-0f72-30c1-bd87-8bbd3080d93d | -11.655 | -47.039 | 2025-10-09 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 128.4 |
| da3b39ca-cd4d-37d1-8938-21f5b9ae49e4 | -8.1804 | -43.3445 | 2025-10-09 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 159.4 |
| 179be3bb-f2d5-37db-85cc-462098a685fd | -11.7215 | -44.3084 | 2025-10-09 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 8673cba2-1e93-3709-beaa-6e6889941dce | -14.2559 | -45.8681 | 2025-10-09 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 143.1 |
| c5d97dc8-e14a-3795-9540-e8fcd555997c | -7.7924 | -44.1998 | 2025-10-09 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 84b03d0d-b4d7-324b-b2f6-b169bac781aa | -8.1618 | -43.323 | 2025-10-09 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 112.5 |
| 4a94b3c0-f713-39d1-943d-91397b1f57ed | -12.425 | -45.7056 | 2025-10-09 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 331.7 |
| 434731b5-9ce2-346e-b0b4-b7564f85f4f0 | -17.6538 | -44.4339 | 2025-10-09 13:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 60991ce2-d6f6-32fd-bf82-238a40652da6 | -10.8919 | -47.1153 | 2025-10-09 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| b8f40867-603a-370b-9633-8f757f4554ff | -11.4682 | -43.4774 | 2025-10-09 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 136.1 |
| f530ab6e-0b8f-328e-85ca-94e6cd896b6f | -10.1199 | -45.4292 | 2025-10-09 13:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 13e4e4af-7f07-300b-8541-04b70956d92e | -11.7833 | -45.1347 | 2025-10-09 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 152.4 |
| bb7322c6-59b4-3afd-9e53-b420bed0d9e5 | -11.6742 | -47.0365 | 2025-10-09 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 0336d51c-5185-3a23-b904-d3017bf47704 | -11.7238 | -46.354 | 2025-10-09 13:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 474296a6-fe1f-3a51-b4ec-6616629d8d38 | -7.8121 | -44.1285 | 2025-10-09 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| bd1da973-323e-339b-b1e4-1b383315934e | -15.8085 | -43.7838 | 2025-10-09 13:40:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 171.3 |
| d3ccc8b8-6ffa-315f-bce0-c420915d5da7 | -10.8729 | -47.1177 | 2025-10-09 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 52eadfa5-d97d-3530-aee5-07ce537d1c01 | -9.3209 | -45.6607 | 2025-10-09 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 745b821f-0ff2-370e-866d-d0a9faf0e6d1 | -13.0586 | -47.8262 | 2025-10-09 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 29fce1fd-c3f6-3492-8b50-a5a90ee100b4 | -11.993 | -45.1958 | 2025-10-09 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 201.4 |
| 1460f161-8fec-3dc8-b3c3-117ffd04fd8e | -16.2788 | -47.1556 | 2025-10-09 13:40:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 1c7cf126-ca5e-3860-97a5-9182ec0aa956 | -10.1386 | -45.4497 | 2025-10-09 13:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 83b19dd1-1cac-3fed-99d2-1d4631dea885 | -10.8922 | -47.093 | 2025-10-09 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 0de46367-d89f-3ad6-9a8d-7981a9e7327b | -15.2384 | -46.3616 | 2025-10-09 13:40:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 87.0 |
| d05f5e12-5e65-3336-a80d-6b9f45250835 | -10.1901 | -44.5703 | 2025-10-09 13:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 232.1 |
| 3f1ff2e0-cbbd-3e7b-a5c5-a141d7643df0 | -12.6964 | -47.6776 | 2025-10-09 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 172.9 |
| 5561b686-2720-3093-a281-2c91d573945d | -10.2095 | -44.5446 | 2025-10-09 13:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 201.4 |
| d12f5810-8e76-3a4c-8036-42161ac2ca75 | -10.1389 | -45.4268 | 2025-10-09 13:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 5776ae83-accf-37a3-a2eb-f4a9a19250cc | -10.1576 | -45.4473 | 2025-10-09 13:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 112.2 |
| b833545f-0ad5-3db9-87af-e93030e9e150 | -12.2525 | -47.8728 | 2025-10-09 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 122.1 |
| a4f7ba09-db62-35e0-9d58-a33fee33ff43 | -16.0946 | -45.7829 | 2025-10-09 13:40:00 | GOES-19 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 25bdeac5-394b-3881-8c1e-f119525e114f | -13.0783 | -47.801 | 2025-10-09 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 4799e028-36f7-3255-bd41-611d4b7420f4 | -7.7927 | -44.1767 | 2025-10-09 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| b0e9a453-7a3c-38a9-88f3-076a18702b2a | -13.2967 | -48.4801 | 2025-10-09 13:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 143.3 |
| d9f89dc2-4f5e-35f7-9c79-c28ba4da2e81 | -8.1807 | -43.321 | 2025-10-09 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 213.4 |
| cf76abdb-68ca-3ee9-97fa-4e63528d996a | -8.199 | -43.3659 | 2025-10-09 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.9 |
| cdeb3125-1524-3145-a752-62b5720f7084 | -9.2979 | -45.9574 | 2025-10-09 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 4ba4defd-0b7c-3878-ab49-f7190303decb | -13.2971 | -48.4579 | 2025-10-09 13:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 177.1 |
| 1eae59f0-598e-3ff7-ae87-4ddbaf415eff | -7.7922 | -44.2229 | 2025-10-09 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 193db908-cc81-3268-bd36-210799b9f332 | -11.785 | -45.0421 | 2025-10-09 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| acea016b-24ab-33b7-8399-5993ae31d5a0 | -10.9109 | -47.1129 | 2025-10-09 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| a20ce132-0c97-33f4-9907-dc592a96a263 | -10.1905 | -44.5471 | 2025-10-09 13:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 201.2 |
| 1164b0ab-1622-3167-9628-2e2d82353fd2 | -10.2092 | -44.5678 | 2025-10-09 13:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 298.1 |
| d2f9f4a5-b9f1-35b3-8349-f3271c6c1df6 | -16.2794 | -47.1327 | 2025-10-09 13:40:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 86.4 |
| adac1256-5fdd-3609-9f01-602498bdd938 | -15.4772 | -47.9578 | 2025-10-09 13:40:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 89.4 |
| fbd83c2f-7859-3f6e-a4f7-8edf98925337 | -13.0976 | -47.7982 | 2025-10-09 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 37d03da6-89fd-388b-a888-5fd98dce26c9 | -8.1804 | -43.3445 | 2025-10-09 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 178.4 |
| 97cfa937-de57-31a9-859f-cb5c6364ad16 | -14.3354 | -52.974 | 2025-10-09 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 90.5 |


[Clique aqui para ver as próximas entradas](README68.md)

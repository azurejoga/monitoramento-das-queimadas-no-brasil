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
| 95b86676-fc23-3e64-b700-826665667609 | -12.73341 | -52.06237 | 2026-07-28 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3e7b3a9-77d9-3e05-9e9e-3db62051c910 | -15.44559 | -41.37559 | 2026-07-28 03:57:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 9a6b3855-5f9a-30f8-b063-997c05646b8b | -15.44226 | -41.37502 | 2026-07-28 03:57:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| fd1628a6-2232-37b1-9523-76dd783227b2 | -18.3764 | -50.68753 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f018516f-b980-3a40-9148-98d9a281c27c | -18.36672 | -50.65808 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3152a06-5caf-3342-85d2-d81efb9b2d41 | -15.24535 | -48.58292 | 2026-07-28 03:57:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e457174-8e6f-31fa-a59d-b46dbde003ce | -12.84765 | -44.38546 | 2026-07-28 03:57:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 1490a63d-fbe3-317c-aa8d-7f6d452d3d79 | -13.39595 | -43.56668 | 2026-07-28 03:57:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff2d494d-e923-3f9b-92c2-9fd4232128f8 | -13.29627 | -45.09398 | 2026-07-28 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 25.6 |
| d2923912-9903-3f88-8319-df498f605df3 | -19.72194 | -47.41286 | 2026-07-28 03:57:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99e4c721-1666-3dbf-bd1f-bee5c77bcd04 | -18.3692 | -50.67268 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a63fb356-f670-39f5-8b1e-847ebb3204eb | -15.24049 | -48.58192 | 2026-07-28 03:57:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8a2b2ca-ac10-3ed8-9727-502dc1fa332d | -16.52598 | -47.73998 | 2026-07-28 03:57:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a3cc2a6-0d42-3ecd-9876-cbc5021aa5b9 | -13.29777 | -45.109 | 2026-07-28 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5143137a-af34-3662-9615-73cce863c75d | -18.37442 | -50.67396 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 601c4d5d-f8a3-3d90-a9de-554a957db88b | -15.45081 | -43.81495 | 2026-07-28 03:57:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e35d6bc3-817b-3415-bf10-51e77265a7c3 | -17.31119 | -42.67533 | 2026-07-28 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 96bd7196-82f8-39e6-8646-be30d24f5406 | -13.30305 | -45.10262 | 2026-07-28 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| b2e7c8b9-03ae-3269-bc9a-62286ee99612 | -12.34194 | -48.22502 | 2026-07-28 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9ee7b56-2e54-3da6-ab43-bfd69919104f | -16.86674 | -49.58393 | 2026-07-28 03:57:00 | NOAA-21 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c756d4ed-272d-3346-8366-6f275d22eb20 | -17.30842 | -42.67092 | 2026-07-28 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| edef130c-ca16-3844-9052-f2ab31520798 | -15.24155 | -48.57648 | 2026-07-28 03:57:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9180a849-894f-3242-832e-540abc2ddf53 | -12.33131 | -47.16188 | 2026-07-28 03:57:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a401aeb5-da46-36dc-8aa6-0fa8b6716695 | -12.45612 | -46.51583 | 2026-07-28 03:57:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8143a849-95fb-36c4-b8f9-2f3687e9dc56 | -18.37153 | -50.68805 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 60ba5cd5-4f94-368e-a587-772898a0c48b | -13.35516 | -54.28689 | 2026-07-28 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a159dd38-f3d7-3007-b97e-d1e9ec8b1cbd | -14.29653 | -45.64377 | 2026-07-28 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8fa89302-7f5a-36d9-814f-093e0987b72c | -17.39953 | -47.33064 | 2026-07-28 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 303e79ea-dde5-37a4-b698-db57fe937cd2 | -13.39476 | -43.56997 | 2026-07-28 03:57:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86a64634-6479-3a75-ac28-d831ad013352 | -18.373 | -50.68088 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b188bf07-4873-3e5f-b957-9ee804ee1c03 | -13.35117 | -54.28699 | 2026-07-28 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| bd7a88c8-3d49-3878-9126-66ac34148c56 | -20.72654 | -40.60148 | 2026-07-28 03:57:00 | NOAA-21 | ANCHIETA | ESPÍRITO SANTO | Brasil | 3200409 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7cfc6acc-5100-3a9c-9ca8-23be46bf7ebd | -18.37864 | -50.67695 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 70bc1135-4ba0-3005-8a66-ccb80eb99246 | -17.60555 | -44.61891 | 2026-07-28 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1e097178-603c-3fe7-a498-10eaea2550f5 | -15.43835 | -41.37807 | 2026-07-28 03:57:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| a3694d45-b741-30df-a83a-fc065cbcc1bc | -18.37622 | -50.66251 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc1649a1-645f-3900-9d72-bfc52ababf40 | -18.37511 | -50.67061 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7601c876-26bf-34dc-9e7d-27cd4be28a2d | -13.29227 | -45.09318 | 2026-07-28 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 25.6 |
| ca28fa47-3cdc-3d12-bbc7-269e1846bbb1 | -19.17138 | -42.99537 | 2026-07-28 03:57:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| a2e2e633-4aba-3f40-bf45-d5ccaa8fcb4b | -12.45603 | -50.54742 | 2026-07-28 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 463d239c-4ed2-3521-b0e4-d3db8e82f812 | -13.30178 | -45.10979 | 2026-07-28 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3afaa21e-299d-36ac-b204-84dfe047a0b3 | -19.79371 | -44.01992 | 2026-07-28 03:57:00 | NOAA-21 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 71ec4361-8b24-3ddd-b2e3-0c686bdc4231 | -12.85065 | -44.39111 | 2026-07-28 03:57:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2b80286c-9389-38b7-860e-9242e3ee4549 | -14.30062 | -45.64453 | 2026-07-28 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cc5bf77e-9423-3698-b9d5-a3959fb44d68 | -13.2984 | -45.10543 | 2026-07-28 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| fe5ae82a-fdf7-30ad-856f-e2e92f83cbcf | -12.45696 | -46.51128 | 2026-07-28 03:57:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4efdcad-0c83-3eec-88dc-4a12171582e6 | -17.40215 | -47.33247 | 2026-07-28 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a365dae7-f276-349e-a29d-71e0d8f59014 | -18.37677 | -50.68924 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 78a4c30e-7516-3e38-b1a4-1027d8df0f95 | -18.37964 | -50.67525 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 58e8b8d5-0209-370d-9882-60a3ddbeab6e | -13.3037 | -45.0812 | 2026-07-28 04:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 93383384-6442-3d99-a55d-2c3e240ada55 | -10.9588 | -43.0565 | 2026-07-28 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 5b214dec-ae33-3c63-b505-fbc48153783b | -13.2838 | -45.1077 | 2026-07-28 04:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 9d4da120-7ab2-3d17-854a-d3b451db8e95 | -10.9401 | -43.0355 | 2026-07-28 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 6f9409d4-88e8-3713-86f9-6b1879e52427 | -20.723 | -49.4242 | 2026-07-28 04:00:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 8d6fe77b-94ae-36cb-a86f-4f73fb2e16fa | -10.9397 | -43.0593 | 2026-07-28 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 227.1 |
| 4ef71d6a-5f4f-36c3-b524-646ad4e360e4 | -13.2843 | -45.0844 | 2026-07-28 04:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| ee4a939d-eb8a-3055-b72d-f3da58c40904 | -13.3032 | -45.1045 | 2026-07-28 04:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 3044d7d5-d751-393f-8cf1-0ea5c95bce42 | -20.59452 | -45.12899 | 2026-07-28 04:00:00 | NOAA-21 | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1a4bb0f3-b948-3694-b884-bc401c13db1c | -20.30443 | -46.35674 | 2026-07-28 04:00:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2dfb4d72-5eca-3e37-a419-23da7beef133 | -22.06107 | -56.52705 | 2026-07-28 04:00:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4eaa5d3a-4e49-3460-b276-3ebf87196425 | -22.68675 | -46.23375 | 2026-07-28 04:00:00 | NOAA-21 | ITAPEVA | MINAS GERAIS | Brasil | 3133600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 12c923f5-98ef-38be-b059-4ebac46cdbcb | -22.557 | -42.11555 | 2026-07-28 04:00:00 | NOAA-21 | CASIMIRO DE ABREU | RIO DE JANEIRO | Brasil | 3301306 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2e1ecedf-2dda-370f-9f9b-84ecddf831d6 | -23.82213 | -46.77061 | 2026-07-28 04:00:00 | NOAA-21 | EMBU-GUAÇU | SÃO PAULO | Brasil | 3515103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7684061e-d850-3ad6-a8b3-163542d49333 | -22.06589 | -56.53547 | 2026-07-28 04:00:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 69e9ad99-4651-3f01-9c0b-e6ccc349129b | -22.05937 | -56.53372 | 2026-07-28 04:00:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d3e75de3-6acc-3ad7-92ae-8a1ab637b7d5 | -21.17171 | -41.86441 | 2026-07-28 04:00:00 | NOAA-21 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 27fe222d-71b3-39fc-833d-5e78916674c5 | -20.98631 | -46.45862 | 2026-07-28 04:00:00 | NOAA-21 | NOVA RESENDE | MINAS GERAIS | Brasil | 3145109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 464d9606-bd9d-3dcf-8afd-c7e0548ed0ef | -22.06616 | -56.53556 | 2026-07-28 04:00:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 11cda0b3-a7b4-30ff-bc5a-da2e23b8e942 | -23.26751 | -44.72137 | 2026-07-28 04:00:00 | NOAA-21 | PARATY | RIO DE JANEIRO | Brasil | 3303807 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0cef7988-14dc-35b4-8ba1-3be4cf18f9e6 | -22.0591 | -56.53359 | 2026-07-28 04:00:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ecfa4bd8-16e4-3a99-84ac-7fdafcc28ca9 | -22.06076 | -56.52689 | 2026-07-28 04:00:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 11.4 |
| eaa496d0-06cc-3f56-aa0e-71915bbd713d | -22.06753 | -56.52884 | 2026-07-28 04:00:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e182bd1b-16b7-3263-b614-c454aac6e8ae | -23.97809 | -48.52488 | 2026-07-28 04:00:00 | NOAA-21 | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 94a374f4-d4e8-3d45-80d5-cd2db8ffdd71 | -22.06784 | -56.52895 | 2026-07-28 04:00:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 52409e5e-f8f1-364f-a755-7a8178e012bc | -23.0191 | -46.67766 | 2026-07-28 04:00:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e8399ec1-d8af-3523-8110-4920e581b117 | -27.34806 | -50.73208 | 2026-07-28 04:02:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 71330577-42e3-3247-9d8e-7d3dc387dd09 | -27.34716 | -50.73036 | 2026-07-28 04:02:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7020dc47-efc8-35b4-bd29-0b6876f9ee15 | -27.68892 | -48.75441 | 2026-07-28 04:02:00 | NOAA-21 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 50654998-ca4f-3b7a-8303-5582fbf4fe04 | -10.9401 | -43.0355 | 2026-07-28 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 0a3ae0e9-69d7-31c5-887b-3224e25f6dd4 | -10.9593 | -43.0326 | 2026-07-28 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| e0339dfc-77af-30e6-8593-a85ac9d56629 | -20.723 | -49.4242 | 2026-07-28 04:10:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 73fa394d-8f0b-3801-a4e7-9776cc9b30e8 | -10.9588 | -43.0565 | 2026-07-28 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 626386bb-d7b8-39fe-b34f-1bd2ff8fcb20 | -13.3032 | -45.1045 | 2026-07-28 04:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| ed049149-df04-3e7e-8c1e-a968aca05299 | -10.9397 | -43.0593 | 2026-07-28 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 215.2 |
| ddc9cf1e-e87b-33ef-a774-db17dfac1e38 | -13.3037 | -45.0812 | 2026-07-28 04:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 24873498-8d22-35fa-994f-d2a5ed29a68c | -13.2843 | -45.0844 | 2026-07-28 04:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| bdb61899-fd3e-301a-a7b8-f97663ebf6d0 | -13.2838 | -45.1077 | 2026-07-28 04:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 718b2772-6328-35c5-827b-03ac015ca7cd | -10.94 | -43.05 | 2026-07-28 04:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 497b247a-d92a-3222-a774-8dc8b215af9c | -10.9588 | -43.0565 | 2026-07-28 04:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| eee8a55d-d4b0-3fa8-8b00-143c325b3447 | -20.723 | -49.4242 | 2026-07-28 04:20:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 37121290-4397-392b-b10f-b0e40ed08abd | -13.3032 | -45.1045 | 2026-07-28 04:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 21177342-eaa5-31d6-a141-ba42979ab5b0 | -18.3743 | -50.6786 | 2026-07-28 04:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 168.8 |
| e243851b-fb85-3991-a35a-16320f2750a7 | -13.3037 | -45.0812 | 2026-07-28 04:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 560f0cf1-123e-3d68-a19c-ee1d6d57d599 | -10.9397 | -43.0593 | 2026-07-28 04:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 255.4 |
| 12f593fb-261f-3ca7-9d96-c04a202e9885 | -20.7223 | -49.4471 | 2026-07-28 04:20:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 2653252c-54bf-3f11-8f35-a8b18c94ff05 | -10.9401 | -43.0355 | 2026-07-28 04:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 46a72632-6b2a-3b3f-bd88-64412417880b | -13.2843 | -45.0844 | 2026-07-28 04:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 2e19705f-67ce-3f6a-b1b2-c065ac712ecf | -18.3749 | -50.6564 | 2026-07-28 04:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 103.2 |
| c499bf9a-6770-3064-abfc-fb5ebd6d520c | -2.42755 | -48.19716 | 2026-07-28 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bbd87df4-2d8c-3d57-b0e4-1df84e73e7db | -3.67445 | -49.48468 | 2026-07-28 04:29:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README12.md)

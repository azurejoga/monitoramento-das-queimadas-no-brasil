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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8762d233-735b-34a0-b604-1beece9beec4 | -8.71124 | -50.04829 | 2025-07-07 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f65ed6e-145e-31aa-a90e-717cf7b78558 | -12.57849 | -56.97797 | 2025-07-07 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 752bea90-757a-3f52-8727-f0d77c09a37f | -7.8294 | -44.1888 | 2025-07-07 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15671c09-227d-339a-89e5-506d8f2211c2 | -12.07116 | -47.98513 | 2025-07-07 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ece20f43-751a-3c96-8e9c-4115f38304be | -11.33381 | -51.44937 | 2025-07-07 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0bbdc82d-1ec2-30d9-bf6f-de6535fe76e1 | -13.01854 | -46.76811 | 2025-07-07 04:34:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e897aac0-338f-348f-a633-c627149926e0 | -9.79799 | -47.73973 | 2025-07-07 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e55eb4b7-e54d-32cb-8a2b-54f5cbea0c36 | -12.57945 | -56.97292 | 2025-07-07 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99f0b3f7-ffee-3d73-a1d7-30e4aaa3f8c4 | -12.48667 | -49.08745 | 2025-07-07 04:34:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da009b84-6fc5-30d0-87b5-457e6363e6c6 | -12.38438 | -47.01684 | 2025-07-07 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d23a7a68-ebae-3490-856f-be174d5b05e1 | -7.69099 | -44.58096 | 2025-07-07 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1084c43e-bfc8-322e-aff8-cdbb696e9ce4 | -8.85771 | -47.95307 | 2025-07-07 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45822372-6d9c-3c28-96cf-e86891e67c22 | -9.19926 | -49.63507 | 2025-07-07 04:34:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 179c949b-390c-332c-8127-31785b07814b | -11.32688 | -51.44821 | 2025-07-07 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df442945-429d-391a-8366-d9523353560e | -7.6947 | -44.58152 | 2025-07-07 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3b87beac-55c4-3b75-b0c6-4a9c2803250f | -9.77203 | -48.26245 | 2025-07-07 04:34:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26fb0fdc-b555-3603-8256-2e5a3a605511 | -7.27178 | -44.61036 | 2025-07-07 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ae70554a-b544-3417-8100-9cd1069b9b1a | -8.74194 | -46.4902 | 2025-07-07 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33ce502b-50c7-3ac9-8968-97ae29fa8ca2 | -10.58056 | -49.12048 | 2025-07-07 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fc4ef452-782e-3854-8e61-2ff95cb7ac31 | -8.32771 | -49.18743 | 2025-07-07 04:34:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b7a1b9d-a688-39b7-961e-c71841c85f1b | -7.70714 | -44.57432 | 2025-07-07 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88133165-b655-38e1-9561-6811a894a306 | -10.65192 | -44.4898 | 2025-07-07 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 947dd757-dd4c-3459-a1be-b3bc0ce696da | -10.94694 | -49.25497 | 2025-07-07 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 38142c95-dd3e-3708-861e-f6ad6e63c58c | -10.95025 | -49.2555 | 2025-07-07 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3339c5bd-f60e-3765-93cc-548580ed244e | -12.06833 | -43.50154 | 2025-07-07 04:34:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dbc89edd-c5a3-3ae1-8dc9-ec079523176d | -14.02136 | -46.2626 | 2025-07-07 04:34:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7f9f42c-a1f1-36b1-965e-5f4e8f2656c9 | -9.44997 | -43.19871 | 2025-07-07 04:34:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f127c4db-6615-3d0f-9f55-6ce433949151 | -10.64079 | -46.38076 | 2025-07-07 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2bb8bbba-a256-3ec3-b3f0-70d22ed6f587 | -13.64801 | -46.81388 | 2025-07-07 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7c1392a-5926-3f0a-9279-d7daa077d272 | -13.10559 | -46.89117 | 2025-07-07 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7947d594-27a5-326a-85ba-d0de36fdd224 | -8.24567 | -46.939 | 2025-07-07 04:34:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e48e06d7-ccaf-3886-b9b0-baa6b7fdaf4d | -10.89034 | -56.45377 | 2025-07-07 04:34:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcbe50d2-5289-358e-a79d-08d967bf83ff | -9.58313 | -57.39663 | 2025-07-07 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a029d9fa-624c-3bac-8778-fb1138fa91b9 | -12.58146 | -56.98022 | 2025-07-07 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 735f76a2-dbe5-3c1a-9757-2b137548050b | -8.06435 | -43.11873 | 2025-07-07 04:34:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| fe760c1d-4e46-33d0-85ed-b81ac84a8c1d | -7.27112 | -44.61485 | 2025-07-07 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f7b56289-de2a-38ff-ac4f-5e2c5cb38459 | -7.38592 | -46.82673 | 2025-07-07 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07dee3ee-89dc-3026-8cd3-479c6350244e | -7.45008 | -46.78077 | 2025-07-07 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| adac7600-ce6b-3a60-bd36-76bdad8b535b | -10.65262 | -44.48485 | 2025-07-07 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d708b678-570b-3670-a78d-879682b1af97 | -11.88212 | -44.88831 | 2025-07-07 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a266c9ce-c7aa-3727-a605-dd2210257e31 | -11.89154 | -44.90512 | 2025-07-07 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 910e94b8-1e88-3ea2-b86a-41937fb29a88 | -14.01771 | -46.26203 | 2025-07-07 04:34:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50f0b6db-9eb9-38e5-92f1-5f675f02bfb0 | -7.68728 | -44.5804 | 2025-07-07 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 048bad31-25a7-3281-8b62-ee36117eb25c | -8.86103 | -47.9536 | 2025-07-07 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8a4f8010-66dd-379b-a78f-0470aa337d93 | -9.20336 | -45.33628 | 2025-07-07 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 234b19ab-70ae-3290-a5bb-2685871fbd62 | -12.02467 | -57.0811 | 2025-07-07 04:34:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| fb6d1334-f83a-3e05-a403-7e402da1e106 | -9.75957 | -53.30208 | 2025-07-07 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b371df15-b353-36f7-9a36-6b82a53dad01 | -14.0314 | -46.24478 | 2025-07-07 04:34:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99745eb1-b280-3b30-a4a8-7e26ad075ce0 | -7.27262 | -44.6554 | 2025-07-07 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49cb70fb-982f-3da5-8506-cbdfbdd60982 | -12.02946 | -57.08198 | 2025-07-07 04:34:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 531c48d2-429f-335e-98c4-d316c13609fc | -7.39265 | -46.82774 | 2025-07-07 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df99480a-180a-3e67-9161-5f1d7d74fc85 | -13.10209 | -46.89051 | 2025-07-07 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| acd51a16-fcd4-39fd-bf8f-0af9a8b247aa | -7.27631 | -44.65586 | 2025-07-07 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0e2d213-8863-3850-8ffe-d245f6f8edc1 | -12.02367 | -57.08643 | 2025-07-07 04:34:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f143c929-841b-3b4e-b03e-c569cddbcd53 | -12.57861 | -56.96916 | 2025-07-07 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aea385ed-7acb-36f3-82b7-b6aa4333ae46 | -9.77588 | -48.25949 | 2025-07-07 04:34:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8903d2a5-0bce-3efa-8db7-c438ce8a072a | -10.12639 | -57.77934 | 2025-07-07 04:34:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 712cbed1-779e-32d7-842b-88ab4d4b3a18 | -10.64874 | -44.48426 | 2025-07-07 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e46b060-f74e-3440-a756-6e6604e5e35b | -12.03045 | -57.07675 | 2025-07-07 04:34:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d56ee225-0222-3e6a-bc6f-7cfe48eaadae | -10.6332 | -46.38358 | 2025-07-07 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b12f22d1-83a6-377d-b51e-dea234f5aa7b | -12.48722 | -49.08393 | 2025-07-07 04:34:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff9f6ee8-7f74-3d0e-ac85-1c1571d8b7e8 | -8.8414 | -48.4957 | 2025-07-07 04:34:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 23913cc1-5c07-3cf7-9655-590d6f4bee25 | -10.64186 | -46.37989 | 2025-07-07 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65a670d8-aaca-3f59-a716-2f384957035a | -12.75351 | -44.41245 | 2025-07-07 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d205413a-3455-316d-b49f-9c06f68a22db | -8.84524 | -48.49276 | 2025-07-07 04:34:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bead7cd3-f7c8-3dae-82b9-a58986af1b99 | -14.01801 | -46.2605 | 2025-07-07 04:34:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03016939-3ac6-3c90-acdc-f59fbdeb5d83 | -7.37377 | -43.70078 | 2025-07-07 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f91a17f1-769a-3c3a-a44b-395b76428592 | -12.02428 | -57.08458 | 2025-07-07 04:34:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 525e43be-7986-3934-9c82-c3313d4609a4 | -8.8447 | -48.49622 | 2025-07-07 04:34:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 32e1f43a-e9ad-3efd-880b-85c20431ddf0 | -7.27327 | -44.65106 | 2025-07-07 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d799641f-cd9c-3b70-ae5d-83daf4eeba1e | -7.70278 | -44.5782 | 2025-07-07 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 88b22aed-b8c6-39f9-87f6-447683b6df0a | -13.01797 | -46.77205 | 2025-07-07 04:34:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa43f53b-3974-365e-b83b-34772df0dd09 | -10.57176 | -49.1334 | 2025-07-07 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0a8166bd-b6bc-3b72-b80b-90e19831b45a | -9.58258 | -57.39968 | 2025-07-07 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 559d1b05-e72c-3c39-b1ea-83bd9bb8f794 | -12.02847 | -57.08726 | 2025-07-07 04:34:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ffff481c-3597-3d3f-8fbb-d2e2d3243f81 | -11.33734 | -49.26123 | 2025-07-07 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96f5a9b8-4a70-3aef-bf1c-20d246020568 | -8.74079 | -46.49776 | 2025-07-07 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74c8bc00-9ccd-33df-bd91-4b5b7d52d6fa | -11.8909 | -44.9097 | 2025-07-07 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48d075b4-5eb3-32e6-b71b-9af314e3381a | -11.33444 | -51.4455 | 2025-07-07 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 597aef8e-1e0e-33c1-b60f-132820a43a0d | -10.57561 | -49.13043 | 2025-07-07 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c206c3b8-f026-36a7-aedc-435905cd6899 | -10.58002 | -49.12397 | 2025-07-07 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d7b593a5-6c11-310c-b396-2c847cc1ed2f | -7.69906 | -44.57765 | 2025-07-07 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd176d42-b9c6-35a4-ba64-f8eb62a7a55b | -10.63379 | -46.37963 | 2025-07-07 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fe63735-e069-3add-a6cb-959e2d0a73b5 | -11.88526 | -44.89394 | 2025-07-07 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7486c69e-e116-3794-a235-3dd6d6be3ce9 | -10.65646 | -46.37812 | 2025-07-07 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 828c8f84-5be5-3783-ae38-05389d6863dd | -7.70343 | -44.57378 | 2025-07-07 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ea8d60bc-1878-3139-a390-2426a075b3d9 | -7.68599 | -44.58921 | 2025-07-07 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 50e71e20-ec11-3d88-b157-fc88ba0461f5 | -11.00105 | -42.78528 | 2025-07-07 04:34:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 190c1eec-09ba-3195-b243-77ab0dd4655a | -8.74136 | -46.49398 | 2025-07-07 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd1a6d06-cd1f-3e0e-8def-ada7c5128a0a | -9.28439 | -50.33166 | 2025-07-07 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 797ade42-418b-3bb0-8e48-378a308ac829 | -13.01971 | -46.76003 | 2025-07-07 04:34:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ca5ddc33-c2f2-3c24-b1aa-9b53e2244408 | -8.86157 | -47.9501 | 2025-07-07 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76d4c874-62a5-3d16-908a-5531a3189d59 | -14.09236 | -49.73926 | 2025-07-07 04:34:00 | NOAA-21 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14455f64-97c4-3409-80b1-be39a90706f8 | -10.6525 | -46.47838 | 2025-07-07 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 525357f9-6aa7-37e9-b9f9-0f89ab7a01e2 | -7.53116 | -43.8272 | 2025-07-07 04:34:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0a2f7f68-ef8e-372b-979c-c50418dad593 | -8.74023 | -46.50151 | 2025-07-07 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3851ed9-4af3-3f93-8116-3935a6a24a71 | -11.33098 | -51.44493 | 2025-07-07 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b69450e-c120-382e-86cd-54b79035e393 | -14.02835 | -46.23989 | 2025-07-07 04:34:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 076e83d3-4ef6-3204-9898-97c67a2d2ccf | -8.71427 | -50.00784 | 2025-07-07 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a30bc92-1e20-3664-83c7-dab226b73d05 | -12.57769 | -56.97422 | 2025-07-07 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README8.md)

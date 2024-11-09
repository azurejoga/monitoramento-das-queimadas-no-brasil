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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a786baf4-b0da-325b-a872-4c7fec64d5ff | -5.04242 | -46.79955 | 2024-11-09 03:40:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02f7d8ff-92c5-3971-97a2-c4f91535c0fb | -3.97852 | -46.41715 | 2024-11-09 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8cbf7aaf-9cd4-3e5d-80f1-d821b4768d22 | -5.19629 | -44.92819 | 2024-11-09 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 50560830-f7aa-3a74-b874-ad9db83ce96a | -4.62858 | -46.53783 | 2024-11-09 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49dbcf6a-d284-3c03-88f1-59047f865cc0 | -8.0726 | -34.9783 | 2024-11-09 03:40:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| feafd8e0-0dff-3e8c-8904-296685e30175 | -7.60742 | -40.43492 | 2024-11-09 03:40:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 553da4fd-21ca-3d55-beae-e1f902c242b4 | -2.36733 | -46.86298 | 2024-11-09 03:40:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 98482e88-ebb8-36e1-95a0-a8044d523c80 | -4.19922 | -45.8685 | 2024-11-09 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 82a06b64-e68f-3df1-ad43-a8c2603d0269 | -3.95735 | -48.17647 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 7ba84e70-acbe-327d-b1bb-a4b6cb862635 | -3.55313 | -47.38722 | 2024-11-09 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bff540a7-c1f1-39a4-8849-d506c632691b | -5.59472 | -37.87058 | 2024-11-09 03:40:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 004282ac-f6f1-3f98-80a5-1768f2dcee63 | -3.54065 | -43.56476 | 2024-11-09 03:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7a49be1b-3b9a-397b-af67-b8b5c4dd2dc1 | -4.4067 | -43.37688 | 2024-11-09 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b77f57e-5a20-31da-b050-f04468cdde03 | -2.42207 | -46.30939 | 2024-11-09 03:40:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8fbf142d-0c89-3059-8246-b6bf46ebfcdd | -3.29598 | -43.54514 | 2024-11-09 03:40:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9e0c21eb-c3bb-35f2-8794-c17c12d52fd2 | -3.24822 | -46.47522 | 2024-11-09 03:40:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70a40133-b576-3f89-84bd-10e8dfdb0b55 | -2.23585 | -46.62058 | 2024-11-09 03:40:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3ae7c4e-0d3d-344b-bd4e-416394880506 | -4.2053 | -45.86956 | 2024-11-09 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b41e28da-7476-3c1f-93ea-f574b0324042 | -1.63302 | -46.11408 | 2024-11-09 03:40:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c2a36b3-26b1-3f17-beea-060690fd0d54 | -4.75035 | -43.86319 | 2024-11-09 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62804d76-8c82-393b-a605-d555b37ae6ea | -2.42127 | -46.30801 | 2024-11-09 03:40:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ef2bff1d-f1eb-3ebd-b1ae-ad7858f37acf | -4.24807 | -47.57431 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 88af267a-82af-3e4c-857c-8eaa7796fe30 | -6.17953 | -45.45362 | 2024-11-09 03:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0cc499ac-0625-3c74-b9f0-d7f388973ecb | -7.10006 | -38.17522 | 2024-11-09 03:40:00 | NOAA-20 | AGUIAR | PARAÍBA | Brasil | 2500205 | 25 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 92387676-7d38-3c50-9cbc-177dc7fe7140 | -6.30282 | -35.06543 | 2024-11-09 03:40:00 | NOAA-20 | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 3a2f706f-063a-3e90-be21-81d7054709c2 | -2.53878 | -47.13239 | 2024-11-09 03:40:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 108847cb-93cc-3bf9-9363-5c171c29c58f | -2.43479 | -46.27393 | 2024-11-09 03:40:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f19daaf5-af75-3cf9-9ac8-48efadef0817 | -6.39667 | -39.71151 | 2024-11-09 03:40:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 743b3123-b084-34e4-8d4c-2aca153113ed | -5.46471 | -43.65388 | 2024-11-09 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2375bbc9-b50b-3b7b-a722-b0aa0d884618 | -8.39239 | -36.2075 | 2024-11-09 03:40:00 | NOAA-20 | SÃO CAITANO | PERNAMBUCO | Brasil | 2613107 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 9eb5f960-589d-3111-a0af-20cd64aa3072 | -5.47085 | -43.6586 | 2024-11-09 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bc364bfe-35a0-39e2-97d6-34d80c2a1a8d | -5.0415 | -46.80465 | 2024-11-09 03:40:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f514d0b4-1553-3165-acb1-e090b1c7c50d | -2.30466 | -46.48779 | 2024-11-09 03:40:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5320c448-dbef-30cd-9a06-e2ebaf4c50d1 | -6.16251 | -43.59093 | 2024-11-09 03:40:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11b2cc56-efb5-37c4-a102-2ec3519c5f78 | -5.4714 | -43.65548 | 2024-11-09 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9a8ce8fd-99da-3474-82b2-52c1dcd0d26b | -6.1377 | -42.80495 | 2024-11-09 03:40:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8f30c4c9-e953-3e9a-8036-3dbbf4baeedd | -3.95056 | -48.16365 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 57078c45-2ce4-3105-a1c6-60273bf90cd6 | -5.19698 | -44.92425 | 2024-11-09 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ca4564eb-528c-33dc-95d5-807222211076 | -7.10891 | -35.01577 | 2024-11-09 03:40:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e1aa0873-2d9e-38bf-8e20-c33090e8faf7 | -5.63119 | -44.83706 | 2024-11-09 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a163d219-cb3b-304f-b384-5ab0313823fe | -9.02964 | -35.41845 | 2024-11-09 03:40:00 | NOAA-20 | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7c688897-acb9-3d0d-abd2-78fec70b35b3 | -5.81663 | -44.12113 | 2024-11-09 03:40:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ac8fc4b-4177-3749-b941-924e44d8fcf8 | -2.23204 | -46.56297 | 2024-11-09 03:40:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a93ef166-9abb-368e-9438-52c6d6eb0433 | -2.17267 | -46.44123 | 2024-11-09 03:40:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78a5869f-c0e7-3fc3-9f99-42f353a7af1b | -2.30524 | -46.48522 | 2024-11-09 03:40:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ab79292-0536-3596-9f32-bdf4b63d2866 | -7.63273 | -43.54286 | 2024-11-09 03:40:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a8917381-b222-3979-9448-4a3dfcb9bb68 | -4.38962 | -47.65062 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f65ac44-6df2-35a9-b604-c6901e09e4ea | -3.29635 | -46.41578 | 2024-11-09 03:40:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| eefd0291-caee-34f8-ac8a-94ad42591114 | -6.23685 | -47.29139 | 2024-11-09 03:40:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63884067-6175-35b1-9369-4f0436eef67b | -4.24703 | -47.5801 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 5bf68519-5761-3e9f-9401-b5d37fa7fd3e | -2.82704 | -47.87086 | 2024-11-09 03:40:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3fde04a7-cec9-302d-8a87-7784b3c3ebf2 | -5.4382 | -43.25951 | 2024-11-09 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5793d36-f54f-3163-8ed6-f8c5f88c64c3 | -6.24746 | -39.71253 | 2024-11-09 03:40:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3066f881-8f90-3458-ac25-080aa0155ef5 | -3.9108 | -46.45506 | 2024-11-09 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 770c8aef-9306-3647-8ca7-5bed149b3502 | -6.53633 | -44.46942 | 2024-11-09 03:40:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9f39be0-dac2-3d84-bd8c-9424d7cbd62c | -4.80663 | -44.93055 | 2024-11-09 03:40:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08eee7f5-f8b4-353e-963e-e46622d3fa90 | -4.43803 | -43.63888 | 2024-11-09 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e03c750a-f47d-377d-a82e-ded158ab8446 | -6.26758 | -41.65452 | 2024-11-09 03:40:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 9588a2df-1a01-3d13-be36-18404efce663 | -3.24584 | -46.48182 | 2024-11-09 03:40:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3564069-0e5a-397a-a389-90daba0f13ad | -5.84903 | -44.08509 | 2024-11-09 03:40:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10ab8b5e-76a1-30d2-9095-1e38292734ad | -6.272 | -41.65536 | 2024-11-09 03:40:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 3f0ce2fe-3f7c-360f-ad5d-685d90fc6601 | -2.10562 | -46.20142 | 2024-11-09 03:40:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d4b3af4-e096-33aa-b86f-ed790c16e044 | -5.46988 | -43.65468 | 2024-11-09 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 03dc0dfb-8830-3587-b194-db27855cf91c | -3.9693 | -48.17999 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 3ca42c53-95f8-3cbc-a123-8a9ee454205d | -5.81078 | -44.12351 | 2024-11-09 03:40:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| dc164161-257e-36e7-b947-efa1874f395c | -2.44682 | -46.31908 | 2024-11-09 03:40:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 57be1516-ea0b-354b-9bd2-1d5fe659a030 | -4.82882 | -47.32517 | 2024-11-09 03:40:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3da05221-9b55-34f2-a4a4-09fc2d621c1f | -6.32429 | -39.51808 | 2024-11-09 03:40:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a4472468-cee4-3a90-97bd-dec044cc852b | -6.39276 | -39.71093 | 2024-11-09 03:40:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 06eb11c5-ac48-3086-9c81-7db90d9b1817 | -5.17344 | -44.00565 | 2024-11-09 03:40:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d272eec8-6b49-3427-91c4-85d24df2e265 | -4.73583 | -43.24979 | 2024-11-09 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8d5a916-4557-38af-b207-5f2fe6f50b68 | -6.23046 | -47.29002 | 2024-11-09 03:40:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ff36742-2b8f-38b2-8586-ace8251882b8 | -5.98477 | -45.37205 | 2024-11-09 03:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ce04325-8fa6-32bb-8e76-a4d51c5c1b2c | -6.24437 | -39.70943 | 2024-11-09 03:40:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e55593f0-2ae7-3ac8-9bc6-f71047268502 | -4.937 | -45.56611 | 2024-11-09 03:40:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b19acd0e-ce2e-381b-ad16-49966a6528d3 | -4.58762 | -37.80717 | 2024-11-09 03:40:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| b83ea330-a80e-3c73-9ec5-87582de6bbb8 | -5.46623 | -43.65469 | 2024-11-09 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a9574e4f-0fa1-33f3-b461-de6fb87f250c | -3.59224 | -42.83925 | 2024-11-09 03:40:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55b74dbe-5248-386a-b9fb-162fb7e4bce2 | -3.50083 | -43.98452 | 2024-11-09 03:40:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97ea0800-49fe-302c-ba0c-d2ba5c24ad60 | -3.53894 | -43.56795 | 2024-11-09 03:40:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 375b7dc2-e698-302e-a3a1-d90dc799924d | -3.55424 | -43.57392 | 2024-11-09 03:40:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ccf3e4ff-079c-36d8-b5e8-9ac117a4955b | -2.36919 | -46.86921 | 2024-11-09 03:40:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4b86b74b-6a38-371e-8e08-4b0a3c77ae2b | -5.4413 | -44.82301 | 2024-11-09 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cfd236a5-0b36-3c20-ab07-6bc7d91894f6 | -6.75954 | -40.53819 | 2024-11-09 03:40:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8784a695-8b32-3001-a76c-7265a0cc62aa | -3.97509 | -48.18811 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| d90746f1-96e3-3f89-b1e2-aa3a363c414a | -5.81133 | -44.12026 | 2024-11-09 03:40:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 93d9d9db-8486-35b0-9e68-00cdad7fbd5f | -7.63168 | -43.54893 | 2024-11-09 03:40:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7254e52e-705b-3b1b-82e2-e088921ce6c0 | -6.24435 | -39.70702 | 2024-11-09 03:40:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d95c0fa8-77b0-3264-9409-8230661db54e | -7.10837 | -35.01923 | 2024-11-09 03:40:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| a3950eb4-976e-3e92-ba71-d226f7ed23de | -3.55367 | -43.57726 | 2024-11-09 03:40:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4b9076ea-1ae7-3b2e-afca-034d201e631a | -4.86838 | -45.68156 | 2024-11-09 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68003c50-ef4c-39f1-84a2-aedc7734e85a | -4.12768 | -43.59458 | 2024-11-09 03:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 04028564-31ac-3314-a031-bb1397b10761 | -5.62562 | -44.83619 | 2024-11-09 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 10c827e5-cc8b-37f5-9a7f-22156a77dda3 | -3.58086 | -47.36138 | 2024-11-09 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1d6ada70-2825-3ad4-a794-2f90e1055526 | -4.23462 | -47.55703 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c72de8a3-b6eb-3a23-bf73-b15a7adb71c9 | -3.5531 | -43.58058 | 2024-11-09 03:40:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3a94cbf2-f361-3f97-8f32-d12b64bb8ae2 | -4.20306 | -46.69728 | 2024-11-09 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6493700-3e0a-3047-821c-b149e883f23b | -3.71301 | -40.71204 | 2024-11-09 03:40:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 472fa4d3-b509-3da5-90f4-183352bb821d | -3.97123 | -46.42168 | 2024-11-09 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 518e04bf-5d50-3df4-97c9-92126caf827b | -5.46678 | -43.65161 | 2024-11-09 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |


[Clique aqui para ver as próximas entradas](README22.md)

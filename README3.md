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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7411f822-f6f0-32c1-a5fe-f163f5971dd5 | -7.59974 | -46.47104 | 2026-06-11 03:36:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f96fc804-d02a-3a51-809b-ae5695a90bdb | -6.43415 | -44.57346 | 2026-06-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f48eb43-fd16-3c12-b809-051d98ea2f0d | -6.18569 | -44.86262 | 2026-06-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69cdd348-49d1-3457-8945-629f7823bd2d | -5.93645 | -43.48363 | 2026-06-11 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd185b12-6166-371d-81ab-ca9472e5723e | -6.43578 | -44.56451 | 2026-06-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 94f3ebd3-7885-3ef5-a0eb-2ed9cfd90fae | -5.04547 | -43.2663 | 2026-06-11 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bb0ed7bb-5008-30d8-a9b9-0af0ea4d7204 | -6.44102 | -44.5698 | 2026-06-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 02535acc-14dc-3e36-9c19-e1f2369ff58c | -6.44547 | -44.57952 | 2026-06-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db39c74a-3eef-32f2-8b08-36541fab4ff6 | -7.72354 | -44.16464 | 2026-06-11 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85b612e1-a883-3c13-af94-082b4621ca1f | -4.36379 | -37.90119 | 2026-06-11 03:36:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6e14b869-753b-39ce-bfc8-6103258b43fc | -6.44709 | -44.57055 | 2026-06-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| fe4daf0d-20ce-3f40-b2e9-0fb53ab42159 | -7.60194 | -46.45943 | 2026-06-11 03:36:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 942d8a87-8755-3f2d-a699-25b44e3d314a | -5.45918 | -37.72525 | 2026-06-11 03:36:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 52201c20-4d71-345f-9c6c-d69628ebf5cf | -5.52128 | -37.62373 | 2026-06-11 03:36:00 | NOAA-21 | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8d8aa8af-166f-3b1b-b386-420281598a45 | -6.44268 | -44.56063 | 2026-06-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| aa20b1c2-486e-3b2c-a9c8-e2cf545ab470 | -5.93575 | -43.48751 | 2026-06-11 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a67cf34-e643-3427-bcb0-625e1d38a335 | -6.43496 | -44.56903 | 2026-06-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a63c365b-49c4-321c-b3ab-3af7a3ea1d1c | -6.44628 | -44.57504 | 2026-06-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c52cbc4f-5640-35d6-851c-90b5277606b1 | -5.61151 | -37.53033 | 2026-06-11 03:36:00 | NOAA-21 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 90d29a3a-48d0-362c-a691-32edc7b8f72e | -6.44791 | -44.56599 | 2026-06-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 940cacdd-605e-360a-889f-954d037d57e2 | -6.44873 | -44.56144 | 2026-06-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| a9d210cd-eea3-3690-8157-08def24c4e85 | -6.95772 | -44.55167 | 2026-06-11 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 50d525ad-3e3b-32d5-881b-2fdd08842ac8 | -7.72425 | -44.16071 | 2026-06-11 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9816e043-b6e7-386c-90d8-9b5accd180ac | -6.95457 | -44.55251 | 2026-06-11 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a2c7525e-38ef-3153-a39b-a3ad0b4a9e62 | -5.28237 | -43.96399 | 2026-06-11 03:36:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3c9b38dc-c903-3abc-9019-967a37dece7b | -7.60084 | -46.46523 | 2026-06-11 03:36:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9686903-7f2b-3fe0-96be-c8de008356e3 | -7.47417 | -36.60462 | 2026-06-11 03:36:00 | NOAA-21 | SERRA BRANCA | PARAÍBA | Brasil | 2515500 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c2ca6d85-d972-349f-9106-dc1539730a5b | -5.03979 | -43.26542 | 2026-06-11 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ae484d1e-2930-3aad-a92f-e57b37049e7e | -6.43335 | -44.57788 | 2026-06-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a16d227c-b65a-3eb5-9f46-23af04be64be | -6.72869 | -39.27579 | 2026-06-11 03:36:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 4eef5493-16d4-3e83-9b03-989d868bd98b | -6.44185 | -44.56522 | 2026-06-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| d1ca3451-5499-3807-a2c2-3b82c437b353 | -6.9553 | -44.54835 | 2026-06-11 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d9986d45-41af-30f5-ba9f-e3791f743c7a | -11.40248 | -37.79875 | 2026-06-11 03:38:00 | NOAA-21 | TOMAR DO GERU | SERGIPE | Brasil | 2807501 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 416e77b0-49bc-3ae7-9c8c-aa1ece1757ed | -12.30434 | -47.91475 | 2026-06-11 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| dcab7c90-3e4e-3f15-92a4-be56370afd55 | -12.6514 | -40.97723 | 2026-06-11 03:38:00 | NOAA-21 | IBIQUERA | BAHIA | Brasil | 2912608 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f6d85c47-acd5-34d5-9b59-b9d027a44abd | -12.85073 | -44.36786 | 2026-06-11 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 470aca96-c879-39df-a552-bbaaea5f2b24 | -11.98139 | -47.38627 | 2026-06-11 03:38:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2ec7cf50-7bd5-31e9-9d14-ff6db07d93b4 | -12.31013 | -47.90428 | 2026-06-11 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c2bd1326-545a-3241-872f-5504e0770dc1 | -9.31688 | -45.48878 | 2026-06-11 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fad87230-e44a-3c5b-84a2-b83bba0ca305 | -9.10983 | -47.9614 | 2026-06-11 03:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1189b2bc-3a99-3acd-905e-ab9f84af6fbf | -12.86002 | -44.37684 | 2026-06-11 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| e71f2f45-47fd-35a6-8226-293e53b2100b | -9.31863 | -45.47953 | 2026-06-11 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 1abfd228-9e76-355c-927d-36827cfd950f | -12.06065 | -45.29093 | 2026-06-11 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b09d5f43-db6e-3bf4-b93f-27c70f9056ed | -11.98061 | -47.38781 | 2026-06-11 03:38:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 050e2d59-d325-3a56-be50-46790af91f47 | -9.31258 | -45.4783 | 2026-06-11 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 1f656e61-4563-3b17-ad46-ecd3f0cd31aa | -15.1791 | -43.85025 | 2026-06-11 03:38:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f7df77f7-2175-3ffe-8fb1-16499492932e | -12.37478 | -47.89345 | 2026-06-11 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb903d10-76b7-3653-a38a-faed684141cc | -9.11164 | -47.96524 | 2026-06-11 03:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c8abbc4c-8969-356c-aae4-a9c03c30cea6 | -12.85537 | -44.37235 | 2026-06-11 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 9995b1d0-61cd-30c2-944e-c152edb959a7 | -15.18313 | -43.84802 | 2026-06-11 03:38:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc7a540f-4028-30e6-a2fe-7e8c52d963a5 | -12.64214 | -43.43857 | 2026-06-11 03:38:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dc503ef9-7554-38cd-b55d-800f78bb531e | -9.30655 | -45.47704 | 2026-06-11 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 69f04ca5-e25a-3c60-bd62-0afb1b6b4721 | -13.36583 | -43.20369 | 2026-06-11 03:38:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 2c2a322d-2997-38b6-bd2e-42e2d7d27696 | -13.36286 | -43.20567 | 2026-06-11 03:38:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ad352770-6afa-32a2-a693-2d7ea2a49784 | -10.99124 | -46.75378 | 2026-06-11 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d541fd73-be42-3496-94a3-65b906b8a6cf | -10.93242 | -44.66686 | 2026-06-11 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6485a796-6284-3b90-b309-66b8e27e7a35 | -15.1771 | -43.85279 | 2026-06-11 03:38:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2019e51e-d982-3728-8f06-35ed0d3c90f1 | -12.86068 | -44.37341 | 2026-06-11 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 0fd0fbf7-fa8d-3d17-915c-a61621ddd549 | -12.15094 | -48.44887 | 2026-06-11 03:38:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c713646c-ae14-37a5-9cdc-6ea93c7a8d18 | -12.14955 | -48.45549 | 2026-06-11 03:38:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea8976cd-c0a0-33c3-88ce-1daf32c686a4 | -12.05415 | -45.29384 | 2026-06-11 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 940ff4a8-02d5-3d45-86f7-48307c547fad | -10.28761 | -47.61518 | 2026-06-11 03:38:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a239b860-900b-388f-9270-826eb09e762d | -12.36817 | -47.89194 | 2026-06-11 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 2b990b87-87f1-3af9-b35c-bc6a8221b72e | -9.32381 | -45.48536 | 2026-06-11 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5ab07291-b45a-3c66-aedc-0d92bce24316 | -10.38295 | -46.62935 | 2026-06-11 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 62508213-0cf6-3d60-bcf6-5170edb85ab6 | -13.36774 | -43.20663 | 2026-06-11 03:38:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f18cb460-dd3d-3d4c-a220-27e0debc9c34 | -9.31601 | -45.4934 | 2026-06-11 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f90962c7-3f7d-3441-adc3-64bbdbcc958e | -9.31951 | -45.47491 | 2026-06-11 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6d0d50b2-11a6-3158-928c-cbf8e40c555e | -9.31346 | -45.47367 | 2026-06-11 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 74dbcd89-08ee-347a-984a-c2a375e23883 | -12.85604 | -44.36892 | 2026-06-11 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| c6a4a7a6-6358-3918-864a-00b66912af64 | -12.14128 | -48.46066 | 2026-06-11 03:38:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d90ef09f-78e3-3768-a216-9bf130f7606d | -12.03428 | -41.38719 | 2026-06-11 03:38:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dca5d1e5-2691-3587-b01a-f18a69d5d9a4 | -8.32065 | -43.81685 | 2026-06-11 03:38:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 53d2bf8d-c719-374a-8f71-91159385f030 | -13.36878 | -43.20101 | 2026-06-11 03:38:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| a4640900-4790-3976-9435-ea5d74b5ae7d | -12.6427 | -43.43559 | 2026-06-11 03:38:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 48750969-a857-3cca-b61d-d3fe3f433a79 | -10.98484 | -46.75272 | 2026-06-11 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75ed0037-23a4-3edc-910a-4524ef1a353c | -9.21143 | -47.91722 | 2026-06-11 03:38:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1a22f356-e934-3678-be01-d1544c22e999 | -9.21318 | -47.91778 | 2026-06-11 03:38:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3ca4b92d-6b9b-3baa-bad9-f225173d9b4a | -12.30223 | -47.90878 | 2026-06-11 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5d7ebf0e-6fd5-353a-a42e-4f82f8dfa46f | -9.31776 | -45.48416 | 2026-06-11 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f7ead62f-1037-371c-ae3d-cf94ce0b0098 | -10.38398 | -46.62413 | 2026-06-11 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ee85cb88-5a93-3240-a7c2-2ba306409eee | -12.05986 | -45.29499 | 2026-06-11 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5eb0aaf3-96d5-3843-b1df-dc2d9d17e4bd | -12.02935 | -47.80106 | 2026-06-11 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| adf11046-b28d-3291-9953-397ee59b1de7 | -12.06634 | -45.29216 | 2026-06-11 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6a3993ec-232d-34c9-9a74-bb652aeca130 | -13.3639 | -43.20006 | 2026-06-11 03:38:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 50776f1c-57fb-3341-9865-0acc591582b6 | -9.32468 | -45.48074 | 2026-06-11 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| ffa4aad7-c0f3-3d0d-98d7-2e04e77dbcff | -12.30562 | -47.90852 | 2026-06-11 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c3f6e69c-cc73-3956-899c-a17b4c020e61 | -9.30742 | -45.47242 | 2026-06-11 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2b5a968c-e9af-3d83-8c8b-8cf12fd001fb | -9.30138 | -45.47116 | 2026-06-11 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 956b8f5a-4797-3914-93da-b25c434b1d19 | -12.04762 | -45.29685 | 2026-06-11 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 96f97c87-790d-3db2-a9d8-15a1e1358387 | -11.57741 | -47.44909 | 2026-06-11 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62d0e8de-34fd-3343-8d2e-d0dc1352397d | -11.58399 | -47.4503 | 2026-06-11 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1760f84-61b7-3477-bd81-101f243b0dc2 | -13.77762 | -47.10715 | 2026-06-11 03:38:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b23b571a-61b6-3e3f-9f56-a5cb227df400 | -11.9818 | -47.38216 | 2026-06-11 03:38:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c945aa7-05f3-3291-bdc1-9b6aa8a05f48 | -12.3088 | -47.91052 | 2026-06-11 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c081f42a-f0fb-3953-85a5-a4e1bb989aaa | -12.86135 | -44.36998 | 2026-06-11 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 88eaa8e2-26a2-3e16-8157-1866afc81bc2 | -6.4357 | -44.5535 | 2026-06-11 03:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| a62f879e-141b-38b2-b564-6b5bdfdba69c | -6.4355 | -44.5764 | 2026-06-11 03:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| e1edcf07-f267-35db-97d9-ba1b755ca9f2 | -9.3234 | -45.4787 | 2026-06-11 03:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| a052265a-587c-3b6c-bff0-5f7bd988a3ba | -20.25744 | -41.85095 | 2026-06-11 03:40:00 | NOAA-21 | MARTINS SOARES | MINAS GERAIS | Brasil | 3140530 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README4.md)

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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26b01910-c83e-335e-95cb-67d823e82dd0 | -8.54053 | -46.32992 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5462205b-0f47-353e-9742-b89ff265673c | -5.12534 | -46.23731 | 2025-10-05 03:53:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb4d1ecc-0a5c-3f2e-9241-b6d86f2d4652 | -4.88173 | -45.85675 | 2025-10-05 03:53:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d3a3e84c-b8fc-34d5-b4ea-928e412af373 | -8.41093 | -45.66159 | 2025-10-05 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9411d230-011a-35a0-b0cb-605ddd5dc43b | -9.32084 | -45.6639 | 2025-10-05 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a420d604-d51d-39b9-afdb-4c507760f5fb | -6.40016 | -43.05933 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9061a6c3-c6c4-3caf-9f80-0fc782bbd207 | -6.12731 | -42.8666 | 2025-10-05 03:53:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 15ff6f3d-3fbc-3c5f-9289-2b568666da87 | -8.859 | -46.83937 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86e161b8-2096-35f7-b24a-f3e74b3909eb | -9.32623 | -45.65977 | 2025-10-05 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 97e7a113-d4be-322d-9e85-487a7c3973ca | -6.16096 | -44.64227 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 696b1dbe-44cc-3717-aecd-f4948759cbf5 | -5.44634 | -42.92044 | 2025-10-05 03:53:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 267a3761-1f6f-39ef-872e-f8443c273788 | -6.37429 | -42.88171 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| aafc6ab8-1862-398e-b1ab-62ad40b11e71 | -10.18946 | -45.53749 | 2025-10-05 03:53:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 742c4650-580d-3c65-adb8-4b718c8c0241 | -9.19881 | -46.92556 | 2025-10-05 03:53:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4ac78e64-72d3-34ba-8c2d-8435b72337c9 | -6.34328 | -41.63616 | 2025-10-05 03:53:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0e399c1e-8b6c-3aa4-b1ca-ee9333a6c4ea | -7.80357 | -44.54903 | 2025-10-05 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 951f1f97-6504-333d-a437-feb7c631da21 | -6.62209 | -42.41253 | 2025-10-05 03:53:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7151d52e-c797-3b52-9dca-55986431015b | -7.7882 | -44.13209 | 2025-10-05 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b029f77a-d4dd-3ffa-a425-e107b38ac20f | -6.0518 | -44.08683 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5f3f1b4b-9309-31e9-84db-8c72c8347201 | -5.82742 | -43.35982 | 2025-10-05 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 794179e6-4d76-3a77-a709-c6df3e13c72d | -5.92869 | -43.32764 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 312e4e0d-e0b1-3936-99ec-a246aeb98e36 | -7.87528 | -42.60215 | 2025-10-05 03:53:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ec4d7001-f067-36db-8488-d3f57013cb35 | -8.84103 | -44.79862 | 2025-10-05 03:53:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae8894ac-4ce2-3979-82b2-76270c849cb6 | -6.07191 | -42.52418 | 2025-10-05 03:53:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5df2a3d0-1ceb-3332-9ece-66ff9f31fd6b | -5.34823 | -45.30509 | 2025-10-05 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 83e52686-c650-3b46-b6e9-7f528f2c913a | -5.77028 | -43.98449 | 2025-10-05 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5009d50a-8e8c-39f3-a468-58e563517d3f | -6.69435 | -42.84253 | 2025-10-05 03:53:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f4328488-270d-35b7-9125-93c2dfc77be4 | -6.2576 | -45.34205 | 2025-10-05 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dc81e881-7df2-39a6-809d-2f9cd9091d1c | -5.58504 | -49.02991 | 2025-10-05 03:53:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 347738f4-08fe-3613-b28f-549338e99cd1 | -7.64421 | -45.49323 | 2025-10-05 03:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f00f4c91-e82d-384c-a716-e8e28c6118b8 | -9.30009 | -45.99069 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9cdc2d94-96fc-37ee-9fd2-23e4606bc092 | -4.25046 | -48.56753 | 2025-10-05 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 942eb95a-a768-3189-84f6-2fbeffeb5e08 | -6.25592 | -45.35184 | 2025-10-05 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 112c117a-ae05-3d6c-9749-0da2108f8545 | -6.2916 | -44.0543 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a0e087b-8f83-3ed8-8ed8-bdf78b787fc3 | -7.79741 | -46.02219 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f7750e0c-95c5-39b0-b6f2-7b9b1ed3dca6 | -8.54788 | -46.31614 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1c6744b1-6e10-30ef-8bea-617a15d1e0d4 | -7.22421 | -42.17709 | 2025-10-05 03:53:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f027d30f-ea50-3727-bb32-82bde46b08a9 | -5.00026 | -47.21646 | 2025-10-05 03:53:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fdde1b4-e570-3c57-9517-79a0471ec949 | -9.91417 | -50.19887 | 2025-10-05 03:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ed721eb-175c-3651-bb2d-a410f96cf8df | -7.15653 | -46.08907 | 2025-10-05 03:53:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| bc6c9fb5-00f8-30d7-814b-8e5a02ec654e | -8.53358 | -46.31349 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ed6aff68-44b0-3a94-8c50-da36d4d4aafd | -8.48015 | -45.91472 | 2025-10-05 03:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b97729c-a111-3787-b415-760948850ae7 | -6.25263 | -45.3709 | 2025-10-05 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5f0ec636-b5f5-3684-9e1c-4bb66be8d031 | -5.96517 | -44.36104 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d71b4afe-5c28-3039-bc36-f354aa95850a | -8.54881 | -46.31098 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9672e75d-534d-360b-af82-63dc9df40549 | -10.19631 | -45.49975 | 2025-10-05 03:53:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09b03766-63e2-3782-a0c3-0040235bbf87 | -5.23414 | -42.98944 | 2025-10-05 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 085b0657-fdde-3b94-95b8-338655f54078 | -5.87331 | -42.53189 | 2025-10-05 03:53:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8ead8e20-4872-3985-ae77-5ef5eead836c | -6.98727 | -47.46978 | 2025-10-05 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e312835f-13c6-3689-a1f7-eb0f05cc2dac | -8.53575 | -46.32907 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 159dd1e1-cf18-3974-9c14-168d9c1fb38f | -7.54603 | -42.41135 | 2025-10-05 03:53:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 67119001-3e5d-36e4-912a-eed4f83f0562 | -6.33522 | -43.46594 | 2025-10-05 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 268e12c2-9b30-33ac-901e-feb87b23690f | -9.97741 | -48.28047 | 2025-10-05 03:53:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc97ea22-44fa-3546-96f6-90c844d240b2 | -6.30338 | -42.4389 | 2025-10-05 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 82867068-047e-3908-8c43-85e13179199d | -6.94393 | -47.04446 | 2025-10-05 03:53:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0de251fb-1907-31da-a744-f287b652c30d | -6.69265 | -42.85275 | 2025-10-05 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 63c9a451-6046-377b-87a0-4eca07db3398 | -6.43869 | -44.15583 | 2025-10-05 03:53:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cb373d2e-a069-35f5-931d-933317af1a30 | -7.10894 | -45.0988 | 2025-10-05 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e6a85617-ddf2-366b-91a2-c3b446ce8439 | -6.19954 | -39.69668 | 2025-10-05 03:53:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 65f82427-6478-3dc5-abad-ce2e1e967ff8 | -6.16164 | -44.66503 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 0341cff8-1506-3032-95c5-ac8920be42fc | -9.25177 | -46.78187 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9d04491e-d9b9-3c0a-be10-9749eacdf4b9 | -8.54029 | -46.33084 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8dce559d-886d-3106-b44e-3f584eeb2e80 | -6.09898 | -43.47911 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08ced72c-778b-3d86-9a0c-1a375e5a53b6 | -10.33352 | -43.73777 | 2025-10-05 03:53:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54a6bb6a-34cb-3349-a7d9-50df62a1b4ac | -5.83719 | -44.44928 | 2025-10-05 03:53:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 40dc6432-c45e-3781-8f6b-95cc66d882b7 | -5.79737 | -42.72221 | 2025-10-05 03:53:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| db200d82-d456-31a3-8c6c-3d8b758ce437 | -5.87637 | -42.53743 | 2025-10-05 03:53:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| e2df3a06-5e9d-3b8d-87d8-1160c11ee846 | -5.83094 | -42.4683 | 2025-10-05 03:53:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2fe6d8c6-e876-3c90-b0cb-2ee8b3e9eb8e | -5.59606 | -43.34469 | 2025-10-05 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 249e4899-14eb-3157-b047-13cafc88e3fb | -8.57927 | -46.30584 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 66d741be-d25d-3c38-a49f-454e3f16654d | -6.40025 | -44.77873 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a8f74fa-1207-35bc-8aa2-68052fc419e9 | -6.40635 | -42.68794 | 2025-10-05 03:53:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6977f5f1-9eed-3336-ba0e-2001531fb393 | -7.05977 | -39.37874 | 2025-10-05 03:53:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5fab3518-a8c4-337d-9f83-a1b0a34ef99d | -8.90166 | -46.68321 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8c79b363-7687-3196-a3dd-5854d7a0c532 | -7.69128 | -42.58754 | 2025-10-05 03:53:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 659ac4b6-72cc-30c4-bd6d-c867009e90f8 | -7.81353 | -44.49131 | 2025-10-05 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a015381a-98b7-3570-888e-b673a22e2f06 | -6.52069 | -42.50945 | 2025-10-05 03:53:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4d3d545b-1012-3015-88aa-11b7c6305906 | -6.35357 | -43.432 | 2025-10-05 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fbe4ccb0-faea-3ca9-886a-33c39d2566a3 | -6.84387 | -45.48737 | 2025-10-05 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e52c870a-b033-3d32-abf0-d10ec8ffd6e2 | -5.98696 | -44.36486 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3231316a-7e09-3aaf-a166-a5101b055100 | -8.5723 | -47.6624 | 2025-10-05 03:53:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc63afc3-104b-3acd-8cf5-19739815bdaa | -5.48211 | -42.80479 | 2025-10-05 03:53:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c9f626c6-fce5-3fbb-81ad-105aab54162a | -5.45543 | -43.4085 | 2025-10-05 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9132d016-268a-316e-b0be-c3c74eead3ec | -6.63685 | -42.80104 | 2025-10-05 03:53:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c0fd2de5-c4ad-3707-8fbe-dcfe08742af8 | -9.95436 | -43.76757 | 2025-10-05 03:53:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cda9c8f0-a64a-3e81-86cf-0ab0d5d3c57f | -5.28083 | -42.85734 | 2025-10-05 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 483587e7-c90a-3606-866d-5ca693147cbf | -6.29888 | -44.44334 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75618e3f-4079-3eb3-8657-2f9dfb5f7f3a | -9.28114 | -45.66901 | 2025-10-05 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4141f1f-80ef-3b67-ad2f-9d8eb98f44d7 | -7.74848 | -46.33147 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dcd3a7b7-c16a-3798-a41d-c29cfa50b0e2 | -7.78417 | -48.43838 | 2025-10-05 03:53:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a98b898-5efa-325e-b9a7-ea6cf690b535 | -8.58512 | -46.32824 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| e2e9f20f-73ff-3c81-9354-0a39daa18c74 | -6.15059 | -44.64954 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 37.6 |
| f356898e-68ba-3e06-b5cf-9789c8058369 | -6.70898 | -42.17027 | 2025-10-05 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0e90037a-67fe-326a-ba1e-cda700a9f46f | -5.91364 | -42.52878 | 2025-10-05 03:53:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f77d4d58-94a5-3bad-8bae-ed41e95637a0 | -7.15482 | -43.26248 | 2025-10-05 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0be9cbbd-6ee7-32e6-a097-d5f3d2ffdc80 | -7.80053 | -42.56062 | 2025-10-05 03:53:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3ed46099-c02c-3d96-ae52-72e79853acff | -5.97388 | -44.36258 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34903e3f-c14e-3301-9c5b-400f577bba2a | -7.51585 | -41.2711 | 2025-10-05 03:53:00 | NOAA-20 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 357fec8f-0cf5-3863-9b28-27bc0ca07f8f | -5.24459 | -42.63963 | 2025-10-05 03:53:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09fa75af-de73-3a3f-95a7-5a600298b6bf | -7.78652 | -44.52016 | 2025-10-05 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README44.md)

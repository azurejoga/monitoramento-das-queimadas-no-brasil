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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5db92e61-ca39-33ce-ae75-842bc3ebf973 | -7.5156 | -45.766602 | 2026-10-09 00:06:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 52ca0880-73ce-302a-a3c9-169531c82919 | -17.615299 | -42.321098 | 2026-10-09 00:06:00 | METOP-B | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8ed1fe96-d36b-3f74-9840-92477d43ddd1 | -2.8957 | -57.201599 | 2026-10-09 00:06:00 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a48c596c-724c-3abb-8299-d5b0363f0db2 | -16.9883 | -41.157101 | 2026-10-09 00:06:00 | METOP-B | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 99fff5e0-1346-3f2e-b455-5c886b59bb5d | -5.9371 | -51.830799 | 2026-10-09 00:06:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a69c1e19-17f7-3c60-a6e3-3329d7a51202 | -9.7344 | -46.977901 | 2026-10-09 00:06:00 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1f79ba5c-6726-3a25-b936-66399f06995c | -6.4543 | -55.490501 | 2026-10-09 00:06:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e761675-3d70-3112-9cf3-6c4484f8411e | -4.9896 | -46.038898 | 2026-10-09 00:06:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e82c1f00-2097-3886-b0cc-dc7d20dbf8a3 | -11.989 | -43.4935 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 04c8e7f1-836a-3c20-8f07-b404dc9efb33 | -9.7925 | -44.774899 | 2026-10-09 00:06:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 707e0da2-2dd4-317b-821e-74955b369470 | -2.9296 | -54.0723 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3775cdd6-a8b9-3227-b4a5-557d962dde80 | -1.5178 | -54.512501 | 2026-10-09 00:06:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91366779-3dcc-309a-8205-a6c6d6a04f6f | -3.3103 | -54.029598 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e800b79d-b792-3a1e-9668-f77f763e5900 | -3.1083 | -53.7677 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34fc5574-3d3f-3121-875e-587aee2ead67 | -9.2804 | -47.431099 | 2026-10-09 00:06:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 48e28f23-e8bb-33ac-a16d-47ae5147e0f8 | -3.3168 | -61.249699 | 2026-10-09 00:06:00 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 02eff0e9-170e-3273-b6fd-58ba682d97e2 | -3.3533 | -50.399899 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f36f8e8b-6a30-3afd-b165-b6437dda8d83 | -9.0407 | -45.8452 | 2026-10-09 00:06:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f9824a58-e289-3733-b5a1-f15fa07ddf4a | -4.5059 | -45.819599 | 2026-10-09 00:06:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e7b0b756-be95-3ad3-98f0-71a44f8056a4 | -9.295 | -47.449699 | 2026-10-09 00:06:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 06b26fe1-1bd0-30cf-9bd1-519ee6542451 | -11.7931 | -46.7775 | 2026-10-09 00:06:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1dbd7f84-83ec-3c25-8beb-e6dab07712c8 | -4.5177 | -54.855701 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a6ec79c-25c2-306c-af49-9f3413d1b5d0 | -4.5768 | -54.938 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2bd0338-5784-38cb-af32-a0a7452609b8 | -2.8759 | -54.154499 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94894ea9-eedb-3695-8af6-06971917a2aa | -10.4104 | -47.275002 | 2026-10-09 00:06:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 23d2335c-f0c8-33ee-9c1a-19735f29e8ff | -15.7297 | -50.792198 | 2026-10-09 00:06:00 | METOP-B | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 51ca0e1b-ab55-3884-8e60-32bd5db39005 | -11.1788 | -45.3162 | 2026-10-09 00:06:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8086e169-16ea-34c2-9fdb-d64c71a5b953 | -13.5934 | -48.577099 | 2026-10-09 00:06:00 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 378b7bb1-3ec1-3633-9623-8ecdddc9147b | -6.9567 | -45.271301 | 2026-10-09 00:06:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7921e7a7-01f2-3f64-9736-a5af3f5d2122 | -4.7419 | -55.6488 | 2026-10-09 00:06:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a50c20b0-13db-388e-b4ed-50fb67c533f1 | -13.3804 | -46.682701 | 2026-10-09 00:06:00 | METOP-B | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 15d0b64c-c5d6-39a9-8c6b-c2eb9f05a158 | -18.529499 | -42.461601 | 2026-10-09 00:06:00 | METOP-B | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 516b8399-7532-3fb3-b131-2c0db779788b | -3.223 | -54.284 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12f23cc4-3c08-3f1b-a554-e12696a54dd1 | -5.9237 | -51.817101 | 2026-10-09 00:06:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e1566e3-5abb-31cf-900d-a7c41058e703 | -2.89 | -54.1716 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e103b15-033e-305b-8d21-0435175ae688 | -14.7798 | -42.8843 | 2026-10-09 00:06:00 | METOP-B | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 9abd0624-08a3-3492-ad42-ff7e0a05cc5b | -2.8973 | -54.0196 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 282907a6-935a-377f-9817-14f1bcadd09b | -3.1123 | -51.023499 | 2026-10-09 00:06:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6604867f-419e-3897-9912-52a15b521027 | -2.0732 | -46.5784 | 2026-10-09 00:06:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b04de65-a716-3528-900f-aad28f20a40c | -4.1291 | -46.869301 | 2026-10-09 00:06:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 58e389e7-4225-3bad-b92f-cb144d7e1508 | -2.9351 | -53.912701 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1484620e-800e-3d12-aa5d-378b69fcad78 | -3.6055 | -54.574902 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad5b89fe-9068-322f-95f3-459a435ef4bf | -13.375 | -43.8876 | 2026-10-09 00:06:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c3d46da8-130e-3ada-ba7a-322d0e480eed | -2.9907 | -54.763401 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb6569ae-5adc-3022-909f-02f8971cd647 | -5.2653 | -50.150902 | 2026-10-09 00:06:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2f96a0e-d8dc-33e9-91a8-20439cd70048 | -5.6361 | -45.802299 | 2026-10-09 00:06:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 66dde542-b4ab-3e85-b773-a136d26cc886 | -2.083 | -46.576199 | 2026-10-09 00:06:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bab977f5-cb4c-3aaf-802f-658e5683ffb7 | -7.2066 | -55.141102 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d7b4c0d-60ea-3ccf-81be-8f6bc7678d13 | -8.9616 | -45.150501 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2c6ba42d-8400-32ed-b7d4-c7f0f24d1e11 | -9.9044 | -44.8559 | 2026-10-09 00:06:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c9402e2c-c23b-3c3b-b101-194db347e301 | -2.334 | -48.491199 | 2026-10-09 00:06:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 812e4695-2e61-3591-96e5-53c9fdc1ea17 | -11.4072 | -47.581299 | 2026-10-09 00:06:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a6fbddf8-3468-3631-aa2d-d504c1d71699 | -5.6896 | -53.464699 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6337db54-25d5-36be-8844-ee61c54d0267 | -4.3221 | -54.897701 | 2026-10-09 00:06:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07cd0a17-5717-3a7f-ba94-7e1c92631bb0 | -13.2586 | -44.007702 | 2026-10-09 00:06:00 | METOP-B | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7b43534d-0406-39c0-8da0-ffc2e416fb05 | -12.0257 | -43.4744 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e9144e61-1dd7-3a23-9011-b44414527996 | -11.1905 | -45.321602 | 2026-10-09 00:06:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7364f1c6-8286-3cec-aa01-39e516816068 | -9.9064 | -44.864399 | 2026-10-09 00:06:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1a89d4d0-5153-3d66-aca7-bceeec407b8c | -4.9817 | -46.0495 | 2026-10-09 00:06:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b1eb3cba-9209-334d-9042-fd18b64c1b83 | -2.7609 | -54.099098 | 2026-10-09 00:06:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06353ba2-56cf-3e4b-893f-9c07a3380767 | -5.9687 | -49.7043 | 2026-10-09 00:06:00 | METOP-B | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b458e0cc-dbe9-31e2-b07a-f33fe6d697d5 | -12.2759 | -48.151699 | 2026-10-09 00:06:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 591cd56a-aa20-3116-9bd3-35c17234b95b | -11.7237 | -43.638199 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b4d41593-46c4-3567-97d9-8149505925a0 | -2.4981 | -56.145199 | 2026-10-09 00:06:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 243f5ad9-239f-3982-990c-92ac1317af34 | -6.9344 | -46.5998 | 2026-10-09 00:06:00 | METOP-B | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 43898f28-81e7-3210-971e-c5f657eb16b2 | -5.094 | -42.659901 | 2026-10-09 00:06:00 | METOP-B | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3b69cf97-cd97-315a-8dfe-617f02d86191 | -7.2477 | -48.0616 | 2026-10-09 00:06:00 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| be01b412-ea81-39fd-86d4-a03c0db61fb5 | -5.1038 | -46.2206 | 2026-10-09 00:06:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| db5b469c-9fca-3390-98ef-2922c0b0cce6 | -5.2971 | -45.719398 | 2026-10-09 00:06:00 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0396fc29-4a0b-3175-8b81-f988e05808a0 | 3.5276 | -51.245499 | 2026-10-09 00:06:00 | METOP-B | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 13554db8-c2a3-3287-b084-3d891ec1a788 | -3.1865 | -50.5746 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd868f9b-8b3d-3632-8575-98877dc0e9d6 | -10.0021 | -48.5779 | 2026-10-09 00:06:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f8afa178-f1cf-3dae-a9c4-f88b772e532c | -6.7235 | -48.114601 | 2026-10-09 00:06:00 | METOP-B | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| e2058578-56ef-36e9-ac24-c344529d6f48 | -6.4864 | -55.305901 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e31f9409-00aa-31c6-9d0d-653e9b446479 | -3.0382 | -54.0989 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43021d4b-b34f-36fe-bbae-02e23b6dd1ad | -3.9144 | -55.839298 | 2026-10-09 00:06:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 889e0a62-34b9-365b-b244-d88cad4ca91d | -10.1522 | -44.68 | 2026-10-09 00:06:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 02a015e6-05ca-30b4-8da9-b0f313d85b66 | 3.5245 | -51.259102 | 2026-10-09 00:06:00 | METOP-B | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 7c8b885d-f3ec-369a-86bd-246b3fcab1ae | -6.9279 | -43.658501 | 2026-10-09 00:06:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fabc5cbd-45da-3f8f-b2ea-3f1b1f8274c5 | -9.6282 | -48.888 | 2026-10-09 00:06:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 24f22233-a76b-3f3f-a28f-2516107883c0 | -11.6133 | -43.694901 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7ffeea30-86c6-37c8-b51f-894edd3c1d15 | -3.9417 | -56.0103 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c31315a-f5ff-308e-b557-ae56b04f7209 | -13.3631 | -43.881302 | 2026-10-09 00:06:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5df22cf9-aa50-31a6-b7e8-5ba1b087bdb4 | -4.0444 | -46.9048 | 2026-10-09 00:06:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8f1a0609-3572-3a1e-86e0-3fbee44b0d06 | -8.9649 | -47.539902 | 2026-10-09 00:06:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fa5432b9-623e-3bd0-bd2b-56bfca3a8ffe | -7.4075 | -44.772701 | 2026-10-09 00:06:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cb4fddfd-f231-38f4-bd60-c4b4c5dfa64d | -3.5934 | -54.566601 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d454ba2-6cd4-3479-bd3d-1afd498fb183 | -11.6203 | -43.594299 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fd6433e6-56d1-31b1-a9f5-724b2f4690be | -6.8951 | -45.8936 | 2026-10-09 00:06:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2ce5e4d1-4a8a-3139-b083-eb7a3b02d5b4 | -11.8462 | -43.588299 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1bf91846-39ed-3da4-803f-3dab9a34502c | -2.9479 | -54.108501 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b475b79-8617-3a1f-9333-8b5bb7f4001c | -5.5917 | -47.266499 | 2026-10-09 00:06:00 | METOP-B | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ddab78a0-4df9-3baa-bcc0-9ba1c61ebda0 | -1.1132 | -54.175999 | 2026-10-09 00:06:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77c560e0-92d4-397e-9ffd-d69eea49d9ed | -7.7526 | -49.205601 | 2026-10-09 00:06:00 | METOP-B | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| e58fc7a6-1f3e-3d4f-9a2b-2ad297d988d2 | -9.8672 | -44.873699 | 2026-10-09 00:06:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 479c57df-5606-3efb-958c-0f1622bfc0e9 | -14.9612 | -47.537998 | 2026-10-09 00:06:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 686b5cf6-d4c6-3d8a-acce-5324017169bd | -2.5438 | -58.009701 | 2026-10-09 00:06:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c9eb1e54-8767-343b-aafe-7c2e65379817 | -3.0109 | -54.115002 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66f87ac6-8d79-38eb-9cf7-5e5c36db142b | -1.3239 | -55.432598 | 2026-10-09 00:06:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5b1fe3d-4d0e-336b-82f8-26ca2325ab83 | -3.0177 | -54.053101 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)

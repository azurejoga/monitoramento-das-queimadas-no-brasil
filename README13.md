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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5f20f8f-259f-32e9-a462-6b808722dd23 | -11.3652 | -55.4408 | 2025-08-16 01:39:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0ead4153-d715-3ae0-8707-c2573c57956a | -11.3584 | -55.4137 | 2025-08-16 01:39:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2758e582-9f27-3c96-a4db-ca5a8ebeab04 | -8.5622 | -63.9156 | 2025-08-16 01:39:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 20209ac7-a734-37d5-b30f-24f1526e9ab9 | -13.1223 | -57.137699 | 2025-08-16 01:39:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3f29d209-9566-30f8-9cef-4f123d3ada91 | -7.5676 | -61.416599 | 2025-08-16 01:39:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| af757822-8eb6-38de-a63e-71d363b21359 | -6.9551 | -59.5546 | 2025-08-16 01:39:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9ec8877a-1c20-3355-9c0b-98078164ab17 | -14.9418 | -54.726002 | 2025-08-16 01:39:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f17b5289-e340-30b4-b201-0cb41d894d8a | -13.1296 | -57.125301 | 2025-08-16 01:39:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5e389e1d-e796-35fe-bcca-f702a5e0f563 | -7.6177 | -63.339298 | 2025-08-16 01:39:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bb883396-8391-3eef-981b-aa3cc03aba46 | -13.4528 | -56.672298 | 2025-08-16 01:39:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eaee36bf-42cf-3f62-867d-70253dcd8250 | -9.1646 | -59.682499 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bc49f02e-07da-3009-8975-d68287c9ad41 | -7.6161 | -63.332401 | 2025-08-16 01:39:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4cc7b4e4-fb8a-31bf-8d57-a9f2162db053 | -8.6662 | -62.465801 | 2025-08-16 01:39:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e09f9977-c21a-33d5-b538-7b4bc003a8aa | -8.9158 | -60.733101 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e6681812-f654-3565-960b-12b7f9634f35 | -8.158 | -62.769501 | 2025-08-16 01:39:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f7724e3f-8a4d-309a-a530-81c65e0e8baf | -11.3554 | -55.443298 | 2025-08-16 01:39:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d3885dd6-3a0e-3d6c-8275-30121556bf5f | -7.5227 | -61.312302 | 2025-08-16 01:39:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 42b4bdfc-0db7-33df-a40d-525328ab7a9b | -8.9767 | -61.707001 | 2025-08-16 01:39:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e9cdc652-438d-3051-9ece-d2cb658e0d94 | -7.6037 | -61.216702 | 2025-08-16 01:39:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f18b7a48-0d71-3e4b-8e04-5026046ad10e | -14.9583 | -54.749802 | 2025-08-16 01:39:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 568ed91a-099d-3627-9e5e-7cfbd36674e9 | -7.9298 | -61.732399 | 2025-08-16 01:39:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 47ba9d98-bf21-3a5a-8c69-5771f2ccea5a | -9.5205 | -60.536598 | 2025-08-16 01:39:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 66f242ed-abb2-35ff-9886-e485f76c523c | -9.2039 | -59.6301 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e901a031-7117-333c-b680-a97a312b7880 | -10.1216 | -57.768799 | 2025-08-16 01:39:00 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 02d3006b-66b1-3644-90f1-32fa26273a04 | -9.0455 | -67.416702 | 2025-08-16 01:39:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 88033645-87a5-3676-9d06-1fb9082adcaa | -6.1457 | -57.936401 | 2025-08-16 01:39:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46d8b58a-c6b6-3b77-877f-3e6574e99c55 | -7.92 | -61.7346 | 2025-08-16 01:39:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f1d47fda-5381-351f-a5ba-3831509d7bf2 | -8.1156 | -61.198299 | 2025-08-16 01:39:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7d33173d-35b7-363c-aa68-5daa86cc9a61 | -8.9337 | -62.237598 | 2025-08-16 01:39:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9ebb75b4-afaf-3cb7-a1ac-7a2da164d9a9 | -14.9515 | -54.7234 | 2025-08-16 01:39:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 837cff05-b395-3f9e-8a02-f5a554738e62 | -9.5222 | -60.544102 | 2025-08-16 01:39:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 98f40212-4ce9-3d71-8b65-ef8091e48876 | -9.0281 | -67.430901 | 2025-08-16 01:39:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e388c4cb-dbf3-3dec-ab6d-2b5df16f63ba | -8.9815 | -60.527901 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 53bf94c8-1502-3e52-8441-2c471fcb4eae | -14.9486 | -54.752399 | 2025-08-16 01:39:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e78557a3-aa27-3683-a9a4-988693200806 | -9.1959 | -59.683701 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3a50c243-5272-3549-94cc-294f86e362f5 | -14.9709 | -54.718102 | 2025-08-16 01:39:00 | METOP-C | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8e366037-6fb9-3b24-8817-eaf0987b2aeb | -8.9703 | -61.678799 | 2025-08-16 01:39:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 83d8721b-6da3-3145-8e65-037b5ac019eb | -13.1199 | -57.127701 | 2025-08-16 01:39:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 885d729c-393e-36ca-bb90-2c3a12915c5d | -6.4846 | -62.938999 | 2025-08-16 01:39:00 | METOP-C | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6e8c85ba-4189-3f36-8916-71e0c90f0b8b | -8.9966 | -60.548302 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 70f45eed-4230-3578-9028-266b7dbccd47 | -8.9922 | -60.4855 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d623bce9-7bd9-3976-bc00-c5cebd408c55 | -8.4684 | -64.047798 | 2025-08-16 01:39:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5d750186-4d10-366a-bc81-40bea46bd374 | -14.968 | -54.7472 | 2025-08-16 01:39:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 00db708d-312d-3896-abad-f5fd5d8e08c7 | -14.935 | -54.699501 | 2025-08-16 01:39:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a6bb12cc-7fb7-3923-9033-767e4cf6311c | -14.9612 | -54.720798 | 2025-08-16 01:39:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c100c118-2eca-37c1-b5e4-ba60ac66c4db | -11.352 | -55.429798 | 2025-08-16 01:39:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 27d99c9b-a912-3d24-8fad-300e8d3b3503 | -9.2175 | -59.6441 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b06beae-12f7-312a-a0f1-86f3f9d90504 | -11.2669 | -50.466099 | 2025-08-16 01:39:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 824ac350-4a28-3d76-86a3-2035e5ed36d6 | -8.9842 | -60.4953 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4a63f75a-e9aa-36ec-8f68-a0de42aa9410 | -8.9983 | -60.555801 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 982e419f-7c86-3f42-9273-e170721d1580 | -7.5693 | -61.423901 | 2025-08-16 01:39:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6b1beb8e-7101-34d1-a5c9-cfc4b22e7d14 | -7.9184 | -61.7276 | 2025-08-16 01:39:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dae051ce-bf99-3a48-8450-e98cec4e406a | -6.9362 | -59.9986 | 2025-08-16 01:39:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ee22bfef-012c-35ce-9e40-23b2a6c1e115 | -8.5638 | -63.9226 | 2025-08-16 01:39:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c6c9e238-8a38-3a11-99fc-2452551df2ec | -9.1725 | -59.628899 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 47384932-85de-3943-9243-2540f3aeec82 | -7.6145 | -63.3256 | 2025-08-16 01:39:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 762dba98-0875-3899-ad77-9a2928fad58a | -7.5359 | -61.3246 | 2025-08-16 01:39:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 24da2f13-d495-32ab-a1de-51b2206d0bcf | -9.3897 | -60.551399 | 2025-08-16 01:39:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 584ee6b5-5b0f-3a27-8efc-18f9c26589ab | -7.6259 | -63.3302 | 2025-08-16 01:39:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2d313597-7243-3789-addf-054f2b483f60 | -22.124399 | -51.4505 | 2025-08-16 01:39:00 | METOP-C | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2a188ea2-d68d-3154-8853-bec7bbb3385b | -14.9578 | -54.7075 | 2025-08-16 01:39:00 | METOP-C | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e687be0f-a283-39a7-b90b-d04ed391ed4c | -9.5124 | -60.546398 | 2025-08-16 01:39:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3354e4c4-1a17-35bd-b73f-0ce43edcb9ea | -8.9885 | -60.558102 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a89775e-5638-370f-871b-d35e083126b0 | -8.9895 | -60.518002 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d963a401-da13-37d4-bbd1-d1febc411712 | -14.9481 | -54.710098 | 2025-08-16 01:39:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a76397e8-aedb-33d7-9d92-7adfbd72e505 | -7.6848 | -63.317001 | 2025-08-16 01:39:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ffed84cc-be2c-3d56-883e-1ace3aac8896 | -8.6646 | -62.4589 | 2025-08-16 01:39:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 85c67c26-71d4-3129-a9f0-eec508378f0a | -8.9913 | -60.5256 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 813eb3c5-9bae-3dd9-8f5d-f2da05869c22 | -7.6054 | -61.223999 | 2025-08-16 01:39:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4cb116fe-cbd3-3955-8d9b-d5ddc617c546 | -9.5026 | -60.548698 | 2025-08-16 01:39:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d957e22b-efa3-3f0e-b81d-79aae37d4673 | -9.5107 | -60.538898 | 2025-08-16 01:39:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dd5b2f92-903d-34ff-bd32-2fb628fb8d45 | -9.1783 | -59.6534 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 88f28151-7c77-3b0a-bcd2-72b3539243a0 | -8.994 | -60.493099 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5d57931a-5306-348a-9f87-04814377b013 | -9.1627 | -59.6744 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| edef9bfd-09b4-3bb9-99fb-72d86a3e8425 | -7.8352 | -61.324402 | 2025-08-16 01:39:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 45a32377-e255-3f4d-834c-4903d1e0e652 | -9.1901 | -59.659302 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f3115a26-be00-34fc-a038-deb27938e17c | -9.0259 | -67.420799 | 2025-08-16 01:39:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 71745d80-f2b0-341a-b814-ccf3894ab271 | -13.1393 | -57.165199 | 2025-08-16 01:39:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dd4106a1-f2e9-3f00-bf07-831849c0840a | -7.8271 | -61.3339 | 2025-08-16 01:39:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 04287072-d332-3213-9223-e5755799e61a | -10.0537 | -59.1189 | 2025-08-16 01:39:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 620c30fd-94ec-3fe9-8dcd-c3f391eb7d8a | -9.0612 | -58.943802 | 2025-08-16 01:39:00 | METOP-C | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1dd208ac-a088-39f6-9563-073c8ba8546c | -7.9119 | -61.743999 | 2025-08-16 01:39:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4c007af8-0ea2-3d47-8c85-d61d5ede8f78 | -9.1978 | -59.691898 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b103a04f-9aa9-3b48-a3d1-423c66a3325b | -8.985 | -60.542999 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c042fa49-958b-3db5-b681-c24576db6b44 | -7.5007 | -63.822601 | 2025-08-16 01:39:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ded895a7-53d1-37c3-a835-9b3b0e6d15cb | -7.5022 | -63.829498 | 2025-08-16 01:39:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4bdf8c6e-6384-3271-9e5d-8efc6ce6e93c | -9.0064 | -60.546001 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eaa64add-145d-3a6e-8123-d37a5c8be3a8 | -6.8026 | -59.826401 | 2025-08-16 01:39:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 949151c9-3642-35ef-8fb0-caf206115fc0 | -8.8962 | -60.737701 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bada4a7c-e066-3555-9f0a-0e953190053d | -7.5342 | -61.317299 | 2025-08-16 01:39:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 390761c6-b306-3eed-bbb2-93107a88e161 | -7.6962 | -63.321701 | 2025-08-16 01:39:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f950eaa9-4024-397d-ae76-11891a224ff9 | -13.4457 | -56.685299 | 2025-08-16 01:39:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2692f7ab-d5fe-3267-8859-ea72cb83ff61 | -9.0477 | -67.426804 | 2025-08-16 01:39:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f76da418-292f-32d1-8b1f-88db0a94407b | -8.993 | -60.533199 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 07984b2d-8777-3409-8e05-edfe8e6a3e7a | -8.9832 | -60.5355 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bbc899f7-00e1-33b2-a2a8-e5b432c78594 | -6.483 | -62.932201 | 2025-08-16 01:39:00 | METOP-C | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d508806b-5ed1-3584-b7d4-27821ad6ace0 | -10.4005 | -64.4981 | 2025-08-16 01:39:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 582cd72a-53f5-31dc-a4ad-35b78dc51d76 | -11.3618 | -55.427299 | 2025-08-16 01:39:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 397c8fc4-b0e7-342e-ae07-f08bbfe43c24 | -8.9686 | -61.671799 | 2025-08-16 01:39:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3d9f2b33-2a4b-3e94-bf3f-5ddbe6766354 | -9.2155 | -59.635899 | 2025-08-16 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README14.md)

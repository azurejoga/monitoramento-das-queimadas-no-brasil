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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a50317f-66a0-326f-96a1-7e6b4be0b19d | -17.7508 | -43.8079 | 2024-10-04 02:56:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 225.4 |
| 99d03676-9262-3bc7-8b36-f4435e752d36 | -17.7515 | -43.7835 | 2024-10-04 02:56:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 73.3 |
| e00e8e7b-28b3-3903-8ebb-5c04071db45a | -18.8606 | -43.6084 | 2024-10-04 02:56:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 90.8 |
| be7b27cd-0f7b-3776-bbd9-1715662a2cec | -18.8613 | -43.5837 | 2024-10-04 02:56:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 149.5 |
| 86b5d6d8-2d29-3936-8c0a-dde49e2a0233 | -18.8816 | -43.5785 | 2024-10-04 02:56:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.3 |
| 1d48a123-fa4a-3076-a08c-88c3c537018d | -19.3159 | -42.5976 | 2024-10-04 02:56:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 136.2 |
| 4f8adc20-e3fa-3f61-b942-3f797d96a7cc | -19.3167 | -42.5724 | 2024-10-04 02:56:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 101.1 |
| f99c918e-125a-36bb-aeaf-9e87a113daf5 | -19.5104 | -42.8691 | 2024-10-04 02:56:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 96.7 |
| d7cff45e-1705-3661-abd6-af69f2bfb893 | -19.8516 | -42.3738 | 2024-10-04 02:56:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 175.7 |
| cfe4dbef-4882-38c4-818e-4fe1111df2af | -20.121 | -43.5219 | 2024-10-04 02:56:56 | GOES-16 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 156.4 |
| 12e8a037-f7e8-387e-897b-db0e8970c0b2 | -20.1218 | -43.4969 | 2024-10-04 02:56:56 | GOES-16 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 87.3 |
| 7dbf9e04-ddb0-3462-b848-d6cfa4692fd1 | -20.1416 | -43.5162 | 2024-10-04 02:56:57 | GOES-16 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 178.3 |
| d4ea80d8-7cd1-3235-a319-02597f02be56 | -20.1424 | -43.4913 | 2024-10-04 02:56:57 | GOES-16 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.4 |
| 11851b6b-f538-392c-89cf-6e787896bd7f | -21.8175 | -48.4346 | 2024-10-04 02:57:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 119.1 |
| a36d9ed2-8b47-3d23-bfa4-5015585f1569 | -22.2684 | -51.4941 | 2024-10-04 02:57:09 | GOES-16 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 86.0 |
| 62bcb511-e401-3e70-b5b8-6f5561ef4764 | -22.269 | -51.4714 | 2024-10-04 02:57:09 | GOES-16 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.9 |
| 42be7710-2420-30cf-a58b-3d0f37035302 | -21.29 | -48.93 | 2024-10-04 03:03:23 | MSG-03 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a30dece4-c52e-3806-b0a8-334269bad511 | -2.8829 | -50.7147 | 2024-10-04 03:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 0adc4ec9-40c2-3843-b836-c1df05e7c850 | -2.9014 | -50.7142 | 2024-10-04 03:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| e1eb1f39-b0f4-340d-93e7-698079c02b07 | -3.3665 | -42.3112 | 2024-10-04 03:05:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 58.2 |
| 3f56cc9d-7b7d-3e91-8fdd-99cd6096d29e | -3.3667 | -42.2875 | 2024-10-04 03:05:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 116.6 |
| 204e9056-2ef2-3523-a963-6e4ef215fa71 | -3.3852 | -42.3103 | 2024-10-04 03:05:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 77.5 |
| 3cb96fba-0f7e-3cb6-8b8e-342cdc2c542d | -3.3854 | -42.2866 | 2024-10-04 03:05:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 153.1 |
| dc5c0ade-4131-3c25-bcb9-548c248e30b3 | -3.2899 | -50.4725 | 2024-10-04 03:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 1e70cdff-3677-3f8e-bc7c-cdd8a9908acc | -3.2899 | -50.4516 | 2024-10-04 03:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 173.8 |
| 7a93c382-8a9d-37cf-a7ab-7dc6e2040419 | -3.3083 | -50.4719 | 2024-10-04 03:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 6c4e8dc0-c21a-3cad-955c-2a78b3f07a84 | -3.3084 | -50.451 | 2024-10-04 03:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 201.2 |
| 6e635ef4-c714-3040-a64c-629c148dcf57 | -3.3269 | -50.4504 | 2024-10-04 03:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 7e048693-2c45-3d04-a090-90edc8d55bd9 | -4.0763 | -48.4902 | 2024-10-04 03:05:29 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 157e8d7a-555c-3df7-a402-4630d8e01962 | -4.0765 | -48.4687 | 2024-10-04 03:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| d1d8c160-2493-365e-bc83-7d7c9f4b254b | -4.0949 | -48.4894 | 2024-10-04 03:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 197.8 |
| eebb2497-ca46-3d24-81b4-b1fe9e7d3730 | -4.095 | -48.4679 | 2024-10-04 03:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| f3e7f91a-80f9-3724-b241-bf2f1d37b879 | -4.5375 | -43.304 | 2024-10-04 03:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| c80885bb-6d15-3367-9231-95014ed9606d | -4.6684 | -45.8961 | 2024-10-04 03:05:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 267886c7-5799-3cff-b5d6-8e0770d43175 | -4.6686 | -45.8738 | 2024-10-04 03:05:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 129.7 |
| 870b74bc-8510-338f-99ee-1a9948f69868 | -4.687 | -45.8951 | 2024-10-04 03:05:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 153.3 |
| 2a7eceb4-f051-348e-95e1-0fbf375254dd | -4.6872 | -45.8727 | 2024-10-04 03:05:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 356.5 |
| 5a768b55-ef3b-38dc-b023-57f184bc3a15 | -5.8216 | -44.1196 | 2024-10-04 03:05:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 85f5830f-3e3e-381d-aa80-479198098f59 | -7.8539 | -45.3611 | 2024-10-04 03:05:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 29a9b82e-0df9-3417-9706-7340355ba034 | -8.6448 | -50.0518 | 2024-10-04 03:05:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 73e65e29-300b-3e3a-abec-bd8f6e3865a8 | -9.0853 | -50.9036 | 2024-10-04 03:05:57 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| a80f58c8-e3cf-37d3-86ba-294029265216 | -9.1039 | -50.9231 | 2024-10-04 03:05:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 10a5fb1f-68fa-3b57-b742-77049540e543 | -9.1041 | -50.902 | 2024-10-04 03:05:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 216.4 |
| 399ce2cc-c1da-350e-b692-f8b5e3ca95c3 | -9.1043 | -50.8808 | 2024-10-04 03:05:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 9d56aabb-a3a8-3275-b7b4-bccefddceaee | -9.3115 | -50.8203 | 2024-10-04 03:05:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| f5423476-42cf-3bf4-abcb-60814daf40f3 | -9.3118 | -50.7991 | 2024-10-04 03:05:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 145.8 |
| a4d3b07a-8b9a-341b-9606-f47100294e23 | -9.3303 | -50.8186 | 2024-10-04 03:05:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 134.0 |
| cbba5335-edb7-3600-982b-b00779f3debb | -9.3306 | -50.7974 | 2024-10-04 03:05:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 256.0 |
| d958a3b6-5c85-3072-8396-4cf0a0f9da95 | -9.845 | -68.9623 | 2024-10-04 03:06:03 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 601ef4f0-dd71-3dac-80c6-eb30d46d05a6 | -11.2566 | -60.5825 | 2024-10-04 03:06:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 463c28ba-5d01-3f09-bd8d-58020b017faa | -11.8242 | -56.6009 | 2024-10-04 03:06:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| c448024e-876f-3659-a796-9248a60a206e | -12.5898 | -53.1359 | 2024-10-04 03:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 94851c9e-b3c8-3f64-a0f1-bb9002e5435d | -12.5901 | -53.115 | 2024-10-04 03:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 6011b45b-c13f-35e2-973f-2292a89feb25 | -12.6092 | -53.1129 | 2024-10-04 03:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 81d33427-ce36-329a-acde-ebccbefeaae7 | -13.079 | -51.1171 | 2024-10-04 03:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 8a517283-fbc2-3b14-8f40-61db064b9154 | -13.0975 | -51.1575 | 2024-10-04 03:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 933f4c35-06ca-3f10-af33-2d8933b38b30 | -13.1166 | -51.1551 | 2024-10-04 03:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 0fd8f865-27f5-34e2-b2e2-1ddd28f85bd1 | -13.117 | -51.1337 | 2024-10-04 03:06:20 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 6426e783-9468-3caf-b909-2237c822259b | -13.1358 | -51.1527 | 2024-10-04 03:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| ed9370d9-fc74-397f-ac65-15e0956418bd | -14.7012 | -48.7782 | 2024-10-04 03:06:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 8d9d8202-c144-3e0f-9080-918d3ca274db | -15.4989 | -49.7345 | 2024-10-04 03:06:33 | GOES-16 | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 451ef364-60a0-3f74-a392-616f2e750c36 | -16.0897 | -50.452 | 2024-10-04 03:06:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 8eddfb46-c628-36da-916a-c0fe1909e4e1 | -16.1094 | -50.4489 | 2024-10-04 03:06:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 3970b2cd-06c8-36ad-8836-3da89cbfe012 | -16.4148 | -57.4028 | 2024-10-04 03:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.9 |
| 6979667b-ec81-31fc-825c-5755f7c3996c | -16.4151 | -57.3823 | 2024-10-04 03:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.7 |
| 5d3e8832-512d-3d7f-947b-81d041a6b590 | -16.5935 | -57.1988 | 2024-10-04 03:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.6 |
| 3329b047-f8d3-3572-b343-4f19cc9b0dac | -16.5938 | -57.1783 | 2024-10-04 03:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.5 |
| 5b9b1638-0717-3954-b7be-003efba18847 | -16.613 | -57.1965 | 2024-10-04 03:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 127.6 |
| 6f04dcec-1475-3dba-a63d-215fdd939e4b | -16.6133 | -57.176 | 2024-10-04 03:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 129.8 |
| ef7a8a51-0e1b-3740-a294-e59dd130c156 | -16.6868 | -57.4741 | 2024-10-04 03:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.5 |
| 3f955006-8624-3cfa-b32f-d75ceaebad0b | -16.6871 | -57.4536 | 2024-10-04 03:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.2 |
| c990df4f-1c84-3d93-971c-a0dad6c0aa65 | -16.7455 | -57.4674 | 2024-10-04 03:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.8 |
| 395d339f-ff18-3ca7-b6ff-22bc9516b075 | -16.765 | -57.4652 | 2024-10-04 03:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.3 |
| dcfadd5b-b3d4-3834-b4ec-07c10c642ceb | -16.9283 | -55.8405 | 2024-10-04 03:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 77.2 |
| 77f40a55-fa47-38da-9398-31a038b8c933 | -16.9287 | -55.8197 | 2024-10-04 03:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 60.1 |
| 7561e6d1-c9fd-3bd9-8a0b-7d744e4c0177 | -17.1574 | -57.3993 | 2024-10-04 03:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.7 |
| 444ea160-43e9-342c-9af3-c01a1931c4fb | -17.1577 | -57.3787 | 2024-10-04 03:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.7 |
| 6c862b53-c0dd-3af0-8f74-352cdc126e63 | -17.1771 | -57.3969 | 2024-10-04 03:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.5 |
| 17ceb886-9181-3750-ac8d-ab8144840c8e | -17.7508 | -43.8079 | 2024-10-04 03:06:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 159.6 |
| c58f3992-9555-3c59-80b4-91fd66cf9798 | -18.8606 | -43.6084 | 2024-10-04 03:06:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 75.8 |
| ad64eda8-b452-34d3-90af-286feab461ad | -18.8613 | -43.5837 | 2024-10-04 03:06:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 140.6 |
| 77cabaeb-5b6e-3547-9913-9e8f8ef12aac | -18.9081 | -42.0315 | 2024-10-04 03:06:50 | GOES-16 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.7 |
| d931a385-c25e-36ad-ac98-df54ca014bbd | -18.9285 | -42.0259 | 2024-10-04 03:06:50 | GOES-16 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.9 |
| cbc5f069-ced3-318e-bbf5-d6a0c314daf1 | -19.3159 | -42.5976 | 2024-10-04 03:06:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 122.8 |
| c1a82393-88f3-31aa-84e3-4e2583d9825b | -19.3167 | -42.5724 | 2024-10-04 03:06:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 93.8 |
| 79191cbb-c610-391c-9828-c7af12ebf53c | -19.3363 | -42.592 | 2024-10-04 03:06:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 91.9 |
| 83285146-858e-3d3e-9e9b-cd6e957eec7d | -19.4899 | -42.8746 | 2024-10-04 03:06:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 92.1 |
| b326e113-5e4b-3cf8-bdb3-1d0f4536f390 | -19.8516 | -42.3738 | 2024-10-04 03:06:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 154.4 |
| 364b2fd8-9e54-32c5-aa25-25f2fcf4babc | -20.121 | -43.5219 | 2024-10-04 03:06:56 | GOES-16 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 104.3 |
| 23af432f-d997-32f6-8457-987fe6ff5ff3 | -20.1218 | -43.4969 | 2024-10-04 03:06:56 | GOES-16 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.6 |
| a409e4c6-fd39-3519-a387-c790a8cff1c4 | -20.4591 | -43.1795 | 2024-10-04 03:06:58 | GOES-16 | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 119.9 |
| 230bbfb6-d5a3-36bc-afde-0c22e808bf05 | -21.7773 | -48.3976 | 2024-10-04 03:07:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 6522faa0-f388-394d-8d3e-c5866a5df5da | -21.778 | -48.3741 | 2024-10-04 03:07:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 96fbb2a3-615c-3fe3-bbe8-d609f54309f2 | -21.7981 | -48.3926 | 2024-10-04 03:07:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 38f4f5b8-6c00-3de7-a4af-e26156ad982d | -21.7988 | -48.3691 | 2024-10-04 03:07:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 636e293f-800d-3ea2-b070-51a7c1406510 | -21.8175 | -48.4346 | 2024-10-04 03:07:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 7959b97b-e80a-3313-beb8-b892058ec4ca | -21.839 | -48.4061 | 2024-10-04 03:07:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 547192bb-7c4b-34a2-bbd2-574666013f6d | -21.8397 | -48.3826 | 2024-10-04 03:07:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 114.1 |
| aff825d9-1efc-39a7-a5db-7d5f6b994263 | -22.2684 | -51.4941 | 2024-10-04 03:07:09 | GOES-16 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.7 |
| c7a315ea-3e70-3b94-9a4a-88f67d2c0359 | -6.21043 | -35.27174 | 2024-10-04 03:13:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |


[Clique aqui para ver as próximas entradas](README48.md)

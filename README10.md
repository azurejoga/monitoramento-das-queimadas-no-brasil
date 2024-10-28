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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56e58da5-15dc-3c9d-bf54-1ebe9ba5bc4b | -4.96037 | -43.21212 | 2024-10-28 00:50:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 721f0b01-9932-3ca4-9875-96ebe38e32d2 | -4.95849 | -43.19921 | 2024-10-28 00:50:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| b84cde18-5c14-33c6-ac37-17da03f39400 | -4.94789 | -43.20072 | 2024-10-28 00:50:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 92590833-7d39-322a-8b95-4f325bb9308b | -4.53742 | -42.98662 | 2024-10-28 00:50:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7ef1ae08-c06b-3dcc-ae15-17387c0a099a | -4.49041 | -42.8947 | 2024-10-28 00:50:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| b7b262e4-6e83-35a0-bf5e-04594617b2b3 | -4.48831 | -42.8807 | 2024-10-28 00:50:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 6854be4c-5db7-3e4f-887e-edbdbd6957d4 | -4.48655 | -42.88757 | 2024-10-28 00:50:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 02f14937-2e1c-3073-af56-53d5a40aed0a | -4.47948 | -42.89631 | 2024-10-28 00:50:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| ff9af368-b9d4-3460-a9b4-782933f676f3 | -4.37001 | -43.17527 | 2024-10-28 00:50:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e956293f-8d71-3ee7-8ec6-e784c593674e | -4.12769 | -42.16148 | 2024-10-28 00:50:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 5ded41f1-5cb8-3ef3-b5d9-ab2e2cb76c58 | -3.87978 | -43.19686 | 2024-10-28 00:50:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 423f3831-a317-3398-8467-eb63023be516 | -3.55637 | -41.41288 | 2024-10-28 00:50:00 | TERRA_M-M | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 25.7 |
| 63d94d1a-3630-3516-b255-7441b14a0bad | -3.55366 | -41.39478 | 2024-10-28 00:50:00 | TERRA_M-M | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 31.4 |
| cce412d6-71f2-340e-9a75-66ca86013fb8 | -13.25809 | -48.24358 | 2024-10-28 00:50:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d33cba8e-a581-31f9-a5fa-3ec1932e8baa | -12.9045 | -44.61108 | 2024-10-28 00:50:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 99d968db-e2ec-3170-bc1d-c6552a4b9420 | -12.89557 | -44.61243 | 2024-10-28 00:50:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 1d1f3c46-c8e8-3f7a-a271-e594eec2047b | -12.89425 | -44.60322 | 2024-10-28 00:50:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 3b282126-3d0c-3141-8e24-602bc1b96e29 | -12.88664 | -44.61377 | 2024-10-28 00:50:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e2afb609-8fd4-35cd-ae53-ac9c55e1f22e | -12.87903 | -44.62439 | 2024-10-28 00:50:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c5f15fcb-dc04-358d-9b94-3a9dbbc3c8a8 | -12.37087 | -43.79501 | 2024-10-28 00:50:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0ddca9ce-ac24-3910-811b-66e7f7370473 | -11.62924 | -44.97364 | 2024-10-28 00:50:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ac85d869-93c2-3e47-abcd-3df1684e2ba0 | -11.62793 | -44.9645 | 2024-10-28 00:50:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 3927cadd-262c-3b41-a87c-aab8dacd6332 | -11.27816 | -45.09724 | 2024-10-28 00:50:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 88db4080-73e0-3477-aaf8-1b87ed252582 | -10.89516 | -44.61267 | 2024-10-28 00:50:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 545b08f7-3be9-3def-96f3-6050dd09b684 | -10.87531 | -44.53861 | 2024-10-28 00:50:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 672289de-defc-3c9b-b64b-6b9af8260d8e | -10.65667 | -45.00865 | 2024-10-28 00:50:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 17f106bb-765e-3f25-a6c9-f3e15d9195f3 | -10.64773 | -45.01002 | 2024-10-28 00:50:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 81b18ecd-71ca-36ed-943c-eb7541992297 | -10.64641 | -45.00079 | 2024-10-28 00:50:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 304f3307-a458-3695-bad1-aac3e5251925 | -10.63746 | -45.00214 | 2024-10-28 00:50:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7bbfcc2c-532a-3eb2-b736-2243c8f845bd | -10.5976 | -44.28043 | 2024-10-28 00:50:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fea4f2eb-f430-347c-a981-827098b75572 | -10.58842 | -44.28182 | 2024-10-28 00:50:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 1790456f-5d61-337e-a2f5-614ac7035082 | -9.67234 | -46.25636 | 2024-10-28 00:50:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 03c1eb8d-b977-3f2a-be8e-605776c7b5b5 | -9.27161 | -47.90783 | 2024-10-28 00:50:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 78d99097-ad6e-3f4a-b768-66346757713e | -9.26248 | -47.90907 | 2024-10-28 00:50:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 95036724-ec12-348c-93fc-e311295c04bd | -8.99476 | -46.76311 | 2024-10-28 00:50:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cf41e1f8-83f0-3396-a8b9-abd1e15dec13 | -8.99353 | -46.7542 | 2024-10-28 00:50:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e99863b6-62de-30bf-9eae-42b6705231d1 | -8.54781 | -47.99972 | 2024-10-28 00:50:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d3b90658-3944-3820-91ef-fe602adaef51 | -8.14126 | -49.48369 | 2024-10-28 00:50:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 3b3f54fa-92a9-3406-b4a7-a37e0adab84b | -7.96278 | -49.05616 | 2024-10-28 00:50:00 | TERRA_M-M | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2d569408-5245-30c3-82e0-2d7a53e05bad | -7.62925 | -47.07734 | 2024-10-28 00:50:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3f619234-209e-3567-a6e3-e59389a634e7 | -7.55721 | -45.90178 | 2024-10-28 00:50:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8f06fadf-ef3e-33cc-8ed5-f29e3835e748 | -7.51337 | -46.63261 | 2024-10-28 00:50:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1504331a-d9cb-3423-9ca8-21471edcf0b4 | -7.4773 | -46.90565 | 2024-10-28 00:50:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 848dc18f-3c32-3a80-953d-dfcd9023e594 | -7.4691 | -46.71711 | 2024-10-28 00:50:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 18fb7147-17dd-31a3-a2e7-f84bc2a6ca23 | -6.44052 | -47.53396 | 2024-10-28 00:50:00 | TERRA_M-M | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| d55ca35b-0f10-33dc-8264-8e7efb54c7cf | -6.36443 | -47.92361 | 2024-10-28 00:50:00 | TERRA_M-M | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ad9bc67a-3653-315b-909d-3c175cd163d4 | -6.1868 | -46.58003 | 2024-10-28 00:50:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 826d40e1-5c41-306b-a1f9-44549f96a2a6 | -6.08026 | -47.20223 | 2024-10-28 00:50:00 | TERRA_M-M | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1ef350c7-3c8f-31b8-9af3-0ac7631e615d | -5.97963 | -45.37262 | 2024-10-28 00:50:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| f6398ee3-abdd-31f3-b759-9d4a322df097 | -5.97826 | -45.36309 | 2024-10-28 00:50:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b546afab-b3d5-33e2-bd81-4c5215b27852 | -5.87651 | -44.1605 | 2024-10-28 00:50:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f24a967d-5f9a-396e-b050-6d9face348c9 | -5.8531 | -46.23691 | 2024-10-28 00:50:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8caf8b94-0b14-3381-9457-fabe16941f81 | -5.83908 | -44.76885 | 2024-10-28 00:50:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3e1de99c-80cc-3d1f-adc7-ce425eb32e2d | -5.83765 | -44.75882 | 2024-10-28 00:50:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c3c456f1-1d73-358e-98e2-990777a999e3 | -5.81994 | -44.12999 | 2024-10-28 00:50:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8143c7da-0dea-3931-9720-41efc9198ce4 | -5.81173 | -44.14233 | 2024-10-28 00:50:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 319d2b2a-b1ee-32d3-b767-1d2203f68118 | -5.81014 | -44.13137 | 2024-10-28 00:50:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| e30e2c53-d73c-374f-9aad-fb3ae455fa6f | -5.78827 | -47.09131 | 2024-10-28 00:50:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cccaccd8-97a9-3158-bc59-e32042792b28 | -5.71765 | -47.11619 | 2024-10-28 00:50:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 876da074-a3e1-3a7c-a18b-2a70500281ca | -5.71642 | -47.10737 | 2024-10-28 00:50:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 849ddc86-4452-37db-8b91-1881129ee5b9 | -5.58201 | -46.33984 | 2024-10-28 00:50:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d770384c-20cf-315b-a664-27e92f01020c | -5.4453 | -45.89367 | 2024-10-28 00:50:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| fcafb0ec-43fc-308e-bc57-21b0d36cadff | -5.41795 | -48.74627 | 2024-10-28 00:50:00 | TERRA_M-M | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| bf1cf3c3-376a-3ac9-a8b3-fd280d9fee55 | -5.40814 | -46.3496 | 2024-10-28 00:50:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f4ae4919-da9d-3e9d-920f-c7641eb1f1a0 | -5.38269 | -48.35215 | 2024-10-28 00:50:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 25e0c307-4f97-3765-b55d-1e836513f7d1 | -5.29449 | -46.32648 | 2024-10-28 00:50:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7ac35814-abda-3f0d-9c80-1f88a98651a5 | -5.29322 | -46.31746 | 2024-10-28 00:50:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 151024a4-8850-3457-a0fa-2aec299fc79f | -5.2915 | -45.14061 | 2024-10-28 00:50:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ac44896e-1120-3bf2-8112-688b0eeccdda | -5.26905 | -46.21064 | 2024-10-28 00:50:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 5ebcc293-3056-3d0c-b880-d06038a53b20 | -5.24629 | -46.70338 | 2024-10-28 00:50:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 035d405c-d6a4-33ef-b3ce-14c711ce41ad | -5.24256 | -46.67678 | 2024-10-28 00:50:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3f3d64e7-6097-3cf0-96e6-e135891e3aba | -5.23843 | -45.41236 | 2024-10-28 00:50:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 543698bd-c17c-31ae-bdc0-afdd8d8d6a46 | -5.23703 | -45.40267 | 2024-10-28 00:50:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 5f2e4445-8ac7-39ca-be9c-ed1191b1d04c | -5.11438 | -46.03154 | 2024-10-28 00:50:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| c7c82f50-15e3-3893-94c0-bf9d8ff29fe5 | -5.11307 | -46.08762 | 2024-10-28 00:50:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b31a76e4-3e23-32c9-b8a0-5b6d6c2783c4 | -5.06602 | -44.22231 | 2024-10-28 00:50:00 | TERRA_M-M | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3d106ba1-3465-31fd-b69d-384f149ac864 | -5.0562 | -44.22384 | 2024-10-28 00:50:00 | TERRA_M-M | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| da8b2b82-3bbf-33c0-adb7-ef26394f88e4 | -5.05617 | -45.81372 | 2024-10-28 00:50:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 13e41d87-bc78-31d9-b04f-cfa8fea28fa1 | -5.0132 | -46.48554 | 2024-10-28 00:50:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1c3ccd30-82a9-38a8-a0eb-30d658f085b0 | -5.00305 | -46.47791 | 2024-10-28 00:50:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 11e701ad-ba5d-364b-8ed7-b3ea9aa66f36 | -4.97575 | -46.48821 | 2024-10-28 00:50:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 43e0f389-123c-3df8-b0e6-3ef80add4b3f | -4.92247 | -49.02679 | 2024-10-28 00:50:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 829c0ce5-69f4-356e-aa49-c83b0d1cf39f | -4.92115 | -49.01716 | 2024-10-28 00:50:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| cc6937a3-65b2-3738-ae93-cc7d4281a4e9 | -4.91478 | -48.63285 | 2024-10-28 00:50:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f753f225-cd54-3b8f-8baa-427bf5c4ccfb | -4.90934 | -48.9992 | 2024-10-28 00:50:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| dfc357cd-53ff-313e-ad8f-90a8584a9266 | -4.90061 | -46.86746 | 2024-10-28 00:50:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3cfe31bb-2348-3d95-9313-561f662aa045 | -4.89938 | -46.85864 | 2024-10-28 00:50:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| aa9d1741-9efe-30fc-abfa-0536d9ac1021 | -4.88889 | -48.64592 | 2024-10-28 00:50:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0daee021-6250-3411-9781-1a4c02e1b1e1 | -4.84034 | -44.94041 | 2024-10-28 00:50:00 | TERRA_M-M | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0e9c5c14-6d87-37a9-9892-ef40df8a8d8f | -4.8322 | -45.5993 | 2024-10-28 00:50:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 70bcc091-3f44-3a81-8eaf-dc76f441856f | -4.81096 | -44.73417 | 2024-10-28 00:50:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 55799e7d-86e8-3591-a836-2e36578f088e | -4.77021 | -46.40161 | 2024-10-28 00:50:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 9f35afae-625d-3959-838b-f223baad2590 | -4.76895 | -46.39264 | 2024-10-28 00:50:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 196.6 |
| 0abfb093-59d6-38c9-b741-4e014e8752c5 | -4.76769 | -46.38363 | 2024-10-28 00:50:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1f692859-a2ca-3d89-abbe-5cbb60f7c8aa | -4.76002 | -46.39385 | 2024-10-28 00:50:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 31f33f91-29de-3074-ab61-b211a30c3a0f | -4.75049 | -44.09803 | 2024-10-28 00:50:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4a2ed654-59ff-3034-874c-617a12075bb5 | -4.75012 | -44.09224 | 2024-10-28 00:50:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| f4f662e9-6d94-3fb8-a4c7-d3b8d430dcf4 | -4.74753 | -50.82626 | 2024-10-28 00:50:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 056068a7-cd4c-37db-a52c-b21496f70972 | -4.74334 | -46.8028 | 2024-10-28 00:50:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4b74bdf8-04d3-3902-87fa-99b3d22fb8fa | -4.73449 | -46.80406 | 2024-10-28 00:50:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |


[Clique aqui para ver as próximas entradas](README11.md)

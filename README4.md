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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20790a5e-4088-3fc1-895f-6e0db0a10322 | -11.81946 | -47.3395 | 2026-05-08 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18fd1dc4-482f-374a-87be-b3cc9964c5fe | -19.17892 | -47.356 | 2026-05-08 04:17:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94e1d9b1-bf37-39d9-bb54-d4e9b3c99197 | -10.66948 | -49.70755 | 2026-05-08 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cae4490e-ff96-3a2b-82b0-2b91e2417e71 | -22.75025 | -43.64855 | 2026-05-08 04:17:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 213861a5-7e82-3bd6-8de2-5156b108cd03 | -11.79108 | -47.098 | 2026-05-08 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d894b6a8-7a59-3b3a-a764-dcaf7a60f7df | -10.67085 | -49.69975 | 2026-05-08 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0dbfb005-4d70-32fd-b22d-a29d6cc67e86 | -10.94086 | -49.4486 | 2026-05-08 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 014a9630-f7c5-352f-8352-fc3a5d4af5f9 | -10.23801 | -52.2278 | 2026-05-08 04:17:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72ab8a28-385e-346e-ab24-17d45552331d | -11.12613 | -45.11367 | 2026-05-08 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0a6d4f78-efc3-35e6-b471-c304a6f3df9b | -11.80592 | -47.09636 | 2026-05-08 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 234e210c-09ab-367a-ac3d-a5b308857fc8 | -11.87008 | -43.86299 | 2026-05-08 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0b0cab5-35ad-39d9-83fd-f08f7250ee4c | -10.04247 | -51.66912 | 2026-05-08 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4bc87a55-268f-37e3-af48-0f1968fd91d2 | -14.13535 | -45.38295 | 2026-05-08 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9fca4c9-140d-39eb-93f5-76fbe1af1067 | -14.13591 | -45.37938 | 2026-05-08 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ed765e8-3729-358c-b6b0-3cc8a6f6180a | -14.1283 | -45.34156 | 2026-05-08 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec43ff75-685f-32c3-a186-64c6d2465413 | -10.05276 | -51.6746 | 2026-05-08 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eba27498-271d-3430-9898-2caa027c09e8 | -15.0378 | -41.99279 | 2026-05-08 04:17:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7e5d7183-674d-3854-a16d-0c0424b3ce20 | -10.0473 | -51.67 | 2026-05-08 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8f5d7d5e-19e1-37f0-80f7-887bd899f075 | -15.6171 | -46.5228 | 2026-05-08 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5e22092a-4d49-3c89-8480-109c03cb55a1 | -8.69995 | -49.07581 | 2026-05-08 04:17:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f74e2427-b090-32f8-a27e-5b4f77558263 | -18.49933 | -55.49558 | 2026-05-08 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c9edb5e9-dc7d-3d3d-baee-37d30065d4c9 | -15.61374 | -46.52221 | 2026-05-08 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a59b298e-8478-3610-a0a6-3111d5ab2c1d | -15.42912 | -43.75853 | 2026-05-08 04:17:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c9227fc6-4148-3244-8e5c-4720dbdebfa6 | -10.04889 | -51.66831 | 2026-05-08 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 581fdf4d-4f2f-3680-9939-81caf22a1124 | -18.51301 | -55.50964 | 2026-05-08 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c6e90f8b-7ceb-3b45-8e04-4dc2d90ef574 | -12.86203 | -43.75689 | 2026-05-08 04:17:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9cfb6f4b-9e73-3fe7-a893-642f6ac13f35 | -11.77078 | -43.64823 | 2026-05-08 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b0d4218-f1e9-3c38-94dc-c200553a8e36 | -21.70119 | -48.41734 | 2026-05-08 04:17:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 19fd60cd-6fa1-334d-b39a-257417ec175d | -11.82017 | -47.33531 | 2026-05-08 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e03c2d6-542b-3f68-bbad-17f30d06aaf4 | -10.04828 | -51.66469 | 2026-05-08 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4aa8999f-833b-333a-85a0-e1a6e2306994 | -12.8543 | -43.76294 | 2026-05-08 04:17:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc3e463b-b247-338d-b320-7bc8628ee6a1 | -11.82375 | -47.33592 | 2026-05-08 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a1f1aeb4-2f15-3639-88f0-82a7d3b6680f | -13.81948 | -48.15448 | 2026-05-08 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1139cdc4-dc6d-3aeb-b771-7d9fb468de33 | -18.50772 | -55.50845 | 2026-05-08 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| db42a290-5fcb-33a5-892c-635221244fa7 | -11.06642 | -49.47393 | 2026-05-08 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8f0ab82-0496-3d17-9ae0-0925868148a2 | -12.41773 | -49.67051 | 2026-05-08 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38a16f9f-f326-3574-af26-4764acf82ca5 | -11.82304 | -47.34012 | 2026-05-08 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e273d5b5-d553-3686-8829-3bd615179171 | -14.13218 | -45.33855 | 2026-05-08 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d74caddd-18d6-3927-994c-3c5666dee710 | -9.29628 | -48.57957 | 2026-05-08 04:17:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c44db3e-9760-3f35-908b-a1f43aeb5528 | -10.04795 | -51.67366 | 2026-05-08 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2162620b-618d-3935-89df-538a6625d642 | -15.61493 | -46.51482 | 2026-05-08 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 916d75e6-69e0-38ce-9412-2258a3354bcd | -10.04407 | -51.6674 | 2026-05-08 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6f27495c-5888-3dff-a271-fbefe7ae60c9 | -14.13437 | -45.34622 | 2026-05-08 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71585bf2-0225-3032-a04c-9baa557af866 | -18.4986 | -55.49905 | 2026-05-08 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1ec9a910-3d47-3a8e-8278-5500f81c2256 | -21.71071 | -48.42323 | 2026-05-08 04:17:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 682d11c6-2f58-3797-a78f-29cddf12cc35 | -8.6925 | -49.09419 | 2026-05-08 04:17:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3041f808-edf6-3df9-acaa-34b0dbba90c6 | -12.34599 | -50.02703 | 2026-05-08 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 311fc240-08a6-3e80-bd6a-232c388f13b0 | -16.15165 | -58.4881 | 2026-05-08 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| a4e05627-9484-3be5-927c-33d0b38117ef | -8.71248 | -47.86511 | 2026-05-08 04:17:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7b3e1dd-c518-37a1-88be-87944ba2c42c | -10.04631 | -51.67535 | 2026-05-08 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bae7dba1-2e8f-3e1a-b023-8488870d9e94 | -9.31158 | -48.5859 | 2026-05-08 04:17:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7b966de7-23cb-3ef2-84f6-b186098e98ba | -10.40952 | -44.93512 | 2026-05-08 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f64eef41-7ad9-3213-8057-59256c815bf1 | -11.79529 | -47.09453 | 2026-05-08 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36f54df2-3266-32cc-85ff-b9fe20d2805d | -9.30761 | -48.58517 | 2026-05-08 04:17:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ca78ead9-abef-3325-84ac-e3e01bba4e0f | -8.71173 | -49.08187 | 2026-05-08 04:17:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a1ccd282-60b7-3fb7-9b75-f4be7269ceec | -10.243 | -52.22874 | 2026-05-08 04:17:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3777429e-8ef6-3dae-8b0e-170bb9677182 | -18.38658 | -51.44001 | 2026-05-08 04:17:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfbabc57-e8c9-3308-a0b0-3724dc30fa4f | -8.79306 | -44.83109 | 2026-05-08 04:17:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0aca5162-c041-35a9-bcde-281abe0b8292 | -8.69666 | -49.09491 | 2026-05-08 04:17:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e318e7ed-1935-3de6-9cb9-0636831c5281 | -9.30026 | -48.58027 | 2026-05-08 04:17:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9b49a3b-3cb6-3a76-b078-03b48bfe39be | -10.87953 | -48.77848 | 2026-05-08 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee8429e4-88f7-3dfe-8a8e-eed93ffa7332 | -14.17842 | -52.88472 | 2026-05-08 04:17:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f6fadcb5-ee5d-3cfa-b0a2-419a938a750b | -9.56204 | -44.57218 | 2026-05-08 04:17:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e687e4f-86d6-3227-81b6-76aa84f3e158 | -9.30364 | -48.58444 | 2026-05-08 04:17:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1d941431-8265-38ec-b500-a8df74ba3cc8 | -21.70184 | -48.41345 | 2026-05-08 04:17:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0681f623-f296-3e89-83fa-9137ba407d8d | -11.47285 | -52.91826 | 2026-05-08 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04f92007-8f1a-34b8-bf20-07da81383354 | -11.94459 | -43.37864 | 2026-05-08 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0812a18f-5f44-38f6-bd39-9006b57b5f42 | -8.78913 | -44.83416 | 2026-05-08 04:17:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ddf9fdc-6f14-3d59-8577-0a10719964be | -9.34828 | -47.0892 | 2026-05-08 04:17:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4f43547-c656-3d6e-8707-36139b828561 | -9.5648 | -44.57624 | 2026-05-08 04:17:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01bb6620-873a-3fcd-bc79-9574fc69bd6c | -20.22298 | -46.83333 | 2026-05-08 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e91de7e-3501-316f-82f9-36798b38932a | -14.13824 | -45.3432 | 2026-05-08 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0ca7c83-fd2b-30be-89e8-23d02494870b | -8.69184 | -49.09801 | 2026-05-08 04:17:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0d27f42b-1ce2-3e11-aaa2-7dbfd428d129 | -15.61097 | -46.51794 | 2026-05-08 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c41f4b53-b5ec-3ebe-b99d-1c77e12a6bf4 | -11.05607 | -44.50407 | 2026-05-08 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6bebb8dc-189a-3216-a3c9-b5ad3b9b23a9 | -10.34903 | -46.42043 | 2026-05-08 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e03c499f-3aa8-33d6-8e2e-d96b48edb13d | -8.696 | -49.09874 | 2026-05-08 04:17:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b68d7a39-2fa6-3185-9a41-a99fe9e3a05b | -11.62857 | -47.88995 | 2026-05-08 04:17:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9bf2e472-6b91-3510-a69f-126659108ef8 | -11.94405 | -43.38219 | 2026-05-08 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c72bf69d-535b-32df-8424-85e75548d459 | -14.13162 | -45.34211 | 2026-05-08 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f23a4ddc-f181-31c0-b049-068c3d981fc9 | -11.47227 | -52.92134 | 2026-05-08 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b33faa96-42af-3795-99f8-3d4c6155929f | -11.77355 | -43.65229 | 2026-05-08 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05ee20cd-6fd0-3c94-9cd3-721bf2efdfdb | -14.13881 | -45.33964 | 2026-05-08 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6540feb-d726-31db-8647-92dc75bd4c42 | -19.7805 | -54.43164 | 2026-05-08 04:17:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4dd41b9-6f34-31c6-9c72-2e255299eeb3 | -8.6958 | -49.07511 | 2026-05-08 04:17:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88340af9-3745-38a6-888e-34e1035daf3d | -13.35356 | -43.08667 | 2026-05-08 04:17:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d36eecd9-cf07-3f48-a251-a94477a89eee | -20.21967 | -46.83271 | 2026-05-08 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2fc94bc2-18ca-3355-87b8-89a518b43fd9 | -12.50125 | -45.4311 | 2026-05-08 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb3612d6-379d-3ed7-8523-3bafc1445349 | -11.77409 | -43.64875 | 2026-05-08 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa51b643-d4d5-30dc-a2ae-ac1f76243e9e | -20.27314 | -45.54978 | 2026-05-08 04:17:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f156d39-0f4a-38da-928b-bdb878443889 | -9.87323 | -44.69118 | 2026-05-08 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81b603bb-6950-3f33-b7e3-08dd7f5e810b | -15.03721 | -41.99699 | 2026-05-08 04:17:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6ea64841-2cfb-30d4-afee-f7056c3960e2 | -8.69732 | -49.09106 | 2026-05-08 04:17:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6876d9e3-88c8-308b-88a0-b92ca50b663b | -11.63303 | -47.88611 | 2026-05-08 04:17:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f47cd97-886a-3145-88f9-0ceeca122d41 | -11.77024 | -43.65176 | 2026-05-08 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2a0df28-310d-3a3d-bc8f-89187e08f670 | -8.69317 | -49.09035 | 2026-05-08 04:17:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b5411d22-36fd-36e0-8d4f-0809bf2a1cba | -11.07103 | -52.47308 | 2026-05-08 04:17:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1194abe0-15bf-33af-b92c-5269f6498117 | -8.6993 | -49.07961 | 2026-05-08 04:17:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7683bebf-0e72-391f-9990-d1a389d1584f | -10.40561 | -44.93814 | 2026-05-08 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87100cea-022d-3bbe-87fc-22347d15c1be | -20.2218 | -46.84074 | 2026-05-08 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README5.md)

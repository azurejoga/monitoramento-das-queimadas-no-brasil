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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94c89b12-ee26-3968-a632-ccc34402a75a | -21.349501 | -55.688 | 2024-10-02 01:22:39 | METOP-C | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| bab02f37-e352-3f31-9d37-24f805875a14 | -21.351101 | -55.695499 | 2024-10-02 01:22:39 | METOP-C | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 70df69ab-4b0e-3a1e-942b-0310303b7a12 | -19.2351 | -46.839401 | 2024-10-02 01:22:39 | METOP-C | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c98b3fb4-0722-37db-a50a-423bcbf45486 | -19.239599 | -46.856201 | 2024-10-02 01:22:39 | METOP-C | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e970390f-3e87-3d2f-93cb-2a2235eccfbe | -19.2255 | -46.8423 | 2024-10-02 01:22:39 | METOP-C | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 317215b3-6e51-3365-beb2-347d0fc5e13a | -19.23 | -46.8591 | 2024-10-02 01:22:39 | METOP-C | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4ad8cbb3-6b13-332a-bd7d-5dde88eb7c89 | -19.234501 | -46.875801 | 2024-10-02 01:22:39 | METOP-C | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 52cbf9c4-af55-3b57-b99b-18fd576ad870 | -18.348101 | -44.008499 | 2024-10-02 01:22:40 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 03acc6e8-946c-3e4b-9d3b-348b975ba8bd | -18.355801 | -44.034901 | 2024-10-02 01:22:40 | METOP-C | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a32b2ca2-41cd-35af-aa0f-7b5ae89d079f | -18.3386 | -44.0116 | 2024-10-02 01:22:40 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bf11396f-b9a4-37fb-b043-2d36c80f560d | -21.427401 | -57.2402 | 2024-10-02 01:22:43 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 25882ff5-b172-3f9b-9e4d-092266dc1043 | -21.415899 | -57.2341 | 2024-10-02 01:22:43 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6bfc0ebb-a4c9-3daf-93f6-4dbd3ddb8230 | -21.417601 | -57.242401 | 2024-10-02 01:22:43 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a28a48be-2df1-35a0-809e-dfc8836b379f | -21.4193 | -57.250702 | 2024-10-02 01:22:43 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 11d88ab3-4d93-3e29-a125-c3884a083ba2 | -21.4062 | -57.236301 | 2024-10-02 01:22:44 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| cae79477-fbb9-3ca7-a836-2d83e55d8360 | -20.0896 | -51.34 | 2024-10-02 01:22:44 | METOP-C | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e613eabd-6477-3649-97e7-b9307692dd85 | -20.7717 | -54.825298 | 2024-10-02 01:22:46 | METOP-C | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9047e00c-3044-3a6a-9c3d-001af92386e6 | -20.7733 | -54.8326 | 2024-10-02 01:22:46 | METOP-C | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| bad0e38e-3c24-3b91-899a-20eb937438d6 | -20.7603 | -54.8204 | 2024-10-02 01:22:46 | METOP-C | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 51a75b28-fa51-3b13-bc32-ca0d974fea72 | -19.262699 | -50.841499 | 2024-10-02 01:22:55 | METOP-C | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d009ddf7-2a5e-30d8-8ae5-3cc286e30e85 | -20.016001 | -55.462898 | 2024-10-02 01:23:00 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6617b29e-7cca-3996-a72a-22685d6a2aa7 | -20.004601 | -55.457901 | 2024-10-02 01:23:00 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 52d73646-de49-394c-82c6-646abd784e95 | -20.006201 | -55.465199 | 2024-10-02 01:23:00 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 494ca8da-c5a6-3b28-9787-214e764f42da | -20.007799 | -55.4725 | 2024-10-02 01:23:00 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0f12a522-5901-3611-9740-4dee515ebbdb | -19.994801 | -55.460201 | 2024-10-02 01:23:00 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a1190a01-bbad-3a08-a229-0d292c4c58ab | -19.996401 | -55.467499 | 2024-10-02 01:23:00 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 284efaec-57b8-3d72-b7af-e4f6976f512f | -19.997999 | -55.4748 | 2024-10-02 01:23:00 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 602d480b-afba-3f0e-b0f9-31f2dfee464f | -20.0415 | -55.960098 | 2024-10-02 01:23:01 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1b8a4a8b-6e19-3292-bb07-56ff8992d3c9 | -20.0431 | -55.967602 | 2024-10-02 01:23:01 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ba13542f-427e-3b9c-869a-7917eb74083e | -20.044701 | -55.974998 | 2024-10-02 01:23:01 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f98944cd-1e7f-3b7b-a897-52b16f12f56a | -19.9851 | -55.462601 | 2024-10-02 01:23:01 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 250b5f82-a806-3df2-a1d5-6dac83568259 | -19.9867 | -55.469898 | 2024-10-02 01:23:01 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5bf688e9-8377-3003-bfb7-b78b913f3c28 | -19.9883 | -55.4772 | 2024-10-02 01:23:01 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 8e1211cf-78b6-36f3-a480-7150645dc857 | -19.9753 | -55.464901 | 2024-10-02 01:23:01 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7ec82877-5e5e-36f0-9a10-abbd824c2f86 | -19.9769 | -55.472198 | 2024-10-02 01:23:01 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 25d929d4-c2dd-37ef-a577-3ece1e9a2e1d | -19.9785 | -55.4795 | 2024-10-02 01:23:01 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 1023357e-8d7f-3ad3-9971-0581d20c0f9e | -19.980101 | -55.486801 | 2024-10-02 01:23:01 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 787f2db2-413b-3e9e-84b1-8858413f645b | -19.9687 | -55.481899 | 2024-10-02 01:23:01 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 48609326-727a-3560-aa1d-c72e009f9f0a | -19.970301 | -55.489201 | 2024-10-02 01:23:01 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 50c8b758-8a9d-30b8-929c-f3970620c15f | -19.7449 | -54.516399 | 2024-10-02 01:23:01 | METOP-C | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 82b9d9db-19b7-3341-9b78-8c085032957f | -19.7465 | -54.523701 | 2024-10-02 01:23:01 | METOP-C | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 936bc8d9-fdb2-3682-a4c0-a50070325cae | -19.9589 | -55.4842 | 2024-10-02 01:23:01 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| fe2a4472-7e8b-38ff-84dc-95dcd3727467 | -19.960501 | -55.4916 | 2024-10-02 01:23:01 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a8bd9b3c-602b-336f-aa2c-c7f1e5f83ee1 | -20.0317 | -55.962399 | 2024-10-02 01:23:02 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fa36c49e-e5ae-38a2-834f-a77a295030ae | -20.036501 | -55.984699 | 2024-10-02 01:23:02 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 86586c2b-60c3-35a9-9539-487589995c7a | -20.015301 | -55.981998 | 2024-10-02 01:23:02 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 249d2285-e525-3e34-a993-518a3dd19fdc | -20.034901 | -55.977299 | 2024-10-02 01:23:02 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ca2be87d-5989-3512-b2c6-1d5bf53968ce | -20.0235 | -55.972198 | 2024-10-02 01:23:02 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cae2d27e-2b6e-3c26-8eee-dd449954cd14 | -20.0137 | -55.974499 | 2024-10-02 01:23:02 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 47abe5b3-7ae8-36f7-a71f-8fc27a0164b4 | -20.0333 | -55.969898 | 2024-10-02 01:23:02 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f176148b-3119-3cdc-ba87-7c36a37ea6bc | -20.025101 | -55.979698 | 2024-10-02 01:23:02 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c6478d15-425d-37d9-b28c-905935488458 | -20.026699 | -55.987099 | 2024-10-02 01:23:02 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 27e48353-50e0-3ff9-af61-c0c1df1fe5f0 | -20.0219 | -55.964802 | 2024-10-02 01:23:02 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4729b058-4799-3ee1-a6ff-375703da2ed2 | -20.3778 | -58.063 | 2024-10-02 01:23:03 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8c22d8bf-0387-3098-9559-2455e27e4ac0 | -20.379601 | -58.0718 | 2024-10-02 01:23:03 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f7cb7924-4c29-335c-ac96-1d634463581b | -19.6586 | -56.474701 | 2024-10-02 01:23:09 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2967b98d-3044-3035-9ed9-3d7275be6dc2 | -19.657 | -56.467098 | 2024-10-02 01:23:09 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 09851a63-1d64-39d7-ae28-0f4aec635440 | -19.647301 | -56.469299 | 2024-10-02 01:23:10 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f0651460-0757-3960-9ad0-7337304580d3 | -19.648899 | -56.476898 | 2024-10-02 01:23:10 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f00464cb-dacc-3b77-8340-ffbd410aa863 | -18.8832 | -54.490398 | 2024-10-02 01:23:15 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| fa57825a-4b0b-3dcd-b85b-5682c4920e95 | -18.8848 | -54.4977 | 2024-10-02 01:23:15 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 46f9ca63-ce10-3884-8c0e-c61c94386f98 | -18.886499 | -54.505001 | 2024-10-02 01:23:15 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9ba518d3-4b18-36b3-a9c5-d1284339533c | -18.8881 | -54.512299 | 2024-10-02 01:23:15 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 8ad9f0be-3f84-3c72-bc61-58ab0beb2b1a | -18.889799 | -54.519501 | 2024-10-02 01:23:15 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 19bc4634-7f70-3863-bc19-ad0995681a8e | -18.8717 | -54.4855 | 2024-10-02 01:23:15 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7f876547-95e0-33e9-8e5d-cfab2aa23470 | -18.8734 | -54.492802 | 2024-10-02 01:23:15 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c7893c0d-4cff-3865-8ca8-e5e59409dc0e | -18.875 | -54.500099 | 2024-10-02 01:23:15 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6807524d-3bba-34c2-8d86-e957d706417b | -18.876699 | -54.507401 | 2024-10-02 01:23:15 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5c2e2beb-0bda-3e89-8cb6-d9ce2f4e9027 | -18.8783 | -54.514702 | 2024-10-02 01:23:15 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 37eba470-85a6-369f-b2d5-070ff77d9d60 | -18.879999 | -54.5219 | 2024-10-02 01:23:15 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 29b729d8-80a0-3295-b09c-53cbdc99b4a9 | -18.867001 | -54.5098 | 2024-10-02 01:23:15 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 8ba603d6-1a42-3189-822d-53560ed14d0b | -18.868601 | -54.517101 | 2024-10-02 01:23:15 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| fed979d1-3658-3f9f-965c-a0366b73c368 | -18.850599 | -54.483101 | 2024-10-02 01:23:15 | METOP-C | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d0212246-7ec5-3ae4-acc8-61f734d45cc6 | -18.816299 | -54.468399 | 2024-10-02 01:23:16 | METOP-C | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| aa6a76cc-d210-3e2a-91df-8680021bb3c0 | -18.818001 | -54.4757 | 2024-10-02 01:23:16 | METOP-C | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| df2550f7-12b5-34a1-b004-632dd0a16a43 | -18.806499 | -54.470798 | 2024-10-02 01:23:16 | METOP-C | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2250936d-fab1-32d4-ae64-b6100643b49c | -18.808201 | -54.4781 | 2024-10-02 01:23:16 | METOP-C | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 31c37ee8-4f82-3b02-83e7-c5294d4329ae | -18.809799 | -54.485401 | 2024-10-02 01:23:16 | METOP-C | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5adb094e-2aa5-3685-8105-af3cffb687d3 | -19.121201 | -57.4753 | 2024-10-02 01:23:22 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 682d2b54-0959-392b-916f-cf11834e5bef | -19.111401 | -57.477501 | 2024-10-02 01:23:22 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1e9b9a07-3343-382a-bf55-34a1d0b0a9ae | -19.113001 | -57.4855 | 2024-10-02 01:23:22 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b1da9ef2-6c7e-3aac-ac21-64ea6010459c | -19.1147 | -57.4935 | 2024-10-02 01:23:22 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1c82bd17-7e45-3994-97c7-1580226db5b4 | -19.1164 | -57.501499 | 2024-10-02 01:23:22 | METOP-C | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ea922224-d6ef-3792-8e55-b5084cf23df7 | -19.1033 | -57.487701 | 2024-10-02 01:23:22 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d4c715bf-ec7e-39a6-aa40-2ebd439728ab | -19.105 | -57.495701 | 2024-10-02 01:23:22 | METOP-C | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0b3ac3cd-271a-35b3-bb69-d2cf2327743d | -19.1066 | -57.5037 | 2024-10-02 01:23:22 | METOP-C | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9a58b288-6664-3ae2-93ba-17dbf5cad5e8 | -18.722601 | -57.334301 | 2024-10-02 01:23:28 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 899e4a6a-1e22-30d5-90ef-a9d375c02fe6 | -18.7243 | -57.342098 | 2024-10-02 01:23:28 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b6f5cb76-f731-3576-a609-c8d16b9fb7e8 | -18.704599 | -57.2976 | 2024-10-02 01:23:28 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 533246ae-9804-3375-bfe3-924c8af8a53f | -18.706301 | -57.305401 | 2024-10-02 01:23:28 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bc697be6-93bb-334b-bfa5-6148d62ba57e | -18.7129 | -57.336601 | 2024-10-02 01:23:28 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f3a5d5e9-bbda-3986-adbf-59a84ccdb0fd | -18.696501 | -57.307598 | 2024-10-02 01:23:28 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fb2eb2c9-8629-3026-ab8a-402757e65c0d | -18.698099 | -57.315399 | 2024-10-02 01:23:28 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4192134d-0e3f-3f6f-b7a1-cf8590b281a8 | -18.6998 | -57.3232 | 2024-10-02 01:23:28 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8fa8c709-0439-3995-83fe-78ac05d021c3 | -18.701401 | -57.331001 | 2024-10-02 01:23:28 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d6f47528-e046-3842-9ba5-5b1119fcc3f0 | -18.690001 | -57.325401 | 2024-10-02 01:23:28 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4c21da44-b491-38bb-9700-67633a6a8cb1 | -18.691601 | -57.333199 | 2024-10-02 01:23:28 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1472e32c-5a94-3b80-9ab3-4ec80cb27926 | -15.7852 | -48.829102 | 2024-10-02 01:23:43 | METOP-C | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ae97bd59-fae5-3a7c-b81e-8d3fc26aee95 | -15.7889 | -48.8433 | 2024-10-02 01:23:43 | METOP-C | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3ecaa47f-c0d5-34a0-8ec8-333344db5b14 | -16.0975 | -50.291199 | 2024-10-02 01:23:44 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README21.md)

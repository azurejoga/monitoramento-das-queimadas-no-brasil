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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 313fd4e8-3dee-303a-9515-68db3bed64fb | -20.31748 | -50.01579 | 2024-10-31 04:29:00 | NPP-375D | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| da01871d-5ca7-33f0-bebd-2167438c53f2 | -20.16792 | -50.72445 | 2024-10-31 04:29:00 | NPP-375D | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7c75f76b-4596-3754-8bf9-40d329f746a7 | -21.68624 | -50.10909 | 2024-10-31 04:29:00 | NPP-375D | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c90031ac-a49a-3593-94a7-9574d2fd1b75 | -24.34957 | -52.16586 | 2024-10-31 04:29:00 | NPP-375D | IRETAMA | PARANÁ | Brasil | 4110805 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 85b0ee75-a9ef-3d87-9a78-7f11dcd18007 | -24.22881 | -52.86933 | 2024-10-31 04:29:00 | NPP-375D | RANCHO ALEGRE D'OESTE | PARANÁ | Brasil | 4121356 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d6543778-19ae-3a70-a2a6-08e7af0a33a0 | -21.56301 | -54.21341 | 2024-10-31 04:29:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a94f4513-633c-362e-88c9-fd7e8165a279 | -21.56177 | -54.2118 | 2024-10-31 04:29:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7172e352-e485-3e4e-8315-67b7c35b9dec | -23.58118 | -54.75681 | 2024-10-31 04:29:00 | NPP-375D | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b558f06e-08a3-3391-83c1-d2690a574721 | -23.99408 | -54.09917 | 2024-10-31 04:29:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 36631543-553f-33cb-8a42-e800b8c4defb | -23.99322 | -54.10384 | 2024-10-31 04:29:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 373dd582-765b-3685-bd15-5e6707fda7ef | -23.99042 | -54.09837 | 2024-10-31 04:29:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 9fceb64a-af0b-3dc0-a98b-959525598ef5 | -23.98956 | -54.10305 | 2024-10-31 04:29:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| f46abe97-b8d7-30ac-8ca9-842b0deab3bf | -23.98675 | -54.09757 | 2024-10-31 04:29:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 06e52296-2e2b-342e-94c5-607a5f5d7bba | -23.98589 | -54.10225 | 2024-10-31 04:29:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 33e09cee-759e-3f67-93ef-975f381c9fc0 | -23.98223 | -54.10146 | 2024-10-31 04:29:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| ad44a667-c9eb-3171-bdda-bf73caa77fcf | -23.98137 | -54.10614 | 2024-10-31 04:29:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| ec265037-4859-3be3-b7fa-3010fe94c4b2 | -23.9777 | -54.10534 | 2024-10-31 04:29:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 0ba40fe8-0318-3f94-ad5b-89e82165af3c | -23.97684 | -54.11003 | 2024-10-31 04:29:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 98ec212a-7513-34f9-816c-cc0987c28ddd | -20.58113 | -55.57131 | 2024-10-31 04:29:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a11e7952-e006-35a7-ae85-03e57d15973c | -21.38101 | -55.7069 | 2024-10-31 04:29:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e798ab52-355a-3870-b829-f2c641b37e4d | -19.46878 | -56.61519 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4c2d0c42-cdb1-3174-97dd-d4f6066c3d05 | -19.46729 | -56.61687 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 69286aff-7ca1-3597-8a0d-619ae419fa87 | -19.47335 | -56.61622 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a76fa4fa-ef13-3d55-86b4-f7b273dc7a84 | -19.47556 | -56.67079 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| bf56282c-529f-3543-bf46-aca7510bbb3f | -19.47041 | -56.64877 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.0 |
| c7daa24b-695a-3c07-a431-8df7c4f63311 | -19.4694 | -56.65377 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.1 |
| 5e19a407-b5eb-3b09-95df-96b8f1badba6 | -19.46582 | -56.64775 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 472f3e43-ac97-3ff1-a2dc-c42039d433e2 | -19.47858 | -56.6558 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5b2838f1-b2ed-38c4-b270-6b2e08fd8a21 | -19.46656 | -56.65112 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 17c11192-1011-3d11-9f20-b0bc6dcd4572 | -19.47644 | -56.61892 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| cb755db7-c6ef-3540-a185-1d7c344d69c4 | -19.47238 | -56.62119 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1f0e89e9-de87-3b1d-a0bb-06a7d448ca5a | -19.46781 | -56.62015 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ea5b2bf1-8442-39ae-b748-8bb7d5c3bf01 | -19.48102 | -56.61995 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 5623b2db-e9a6-3365-9479-b87cf7fe353e | -19.47186 | -56.6179 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| a8665d72-cbf8-3110-98ca-dd1f62e88ecf | -19.47142 | -56.64379 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 53afa246-5d3a-3fd6-b756-16afc75f0bd5 | -19.46753 | -56.64612 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 543a6027-b922-3ebd-b1fe-f9de8b69fee8 | -19.5829 | -56.62884 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 625cea91-8418-3c2b-891d-e3a449c064c0 | -19.50627 | -56.58939 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 8d1cf658-b85d-343e-b314-52e88826a62a | -19.50528 | -56.59433 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| de73f34e-179b-3dc8-9558-2b7871634390 | -19.50368 | -56.5785 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 0e12ae96-57b7-377c-83a5-9667d1764cc9 | -19.5033 | -56.60422 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 950a26ef-29e1-3675-9f95-d0179d8d7545 | -19.50269 | -56.58343 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 0a7c5021-b376-33a1-a9a8-d4200362545a | -19.50071 | -56.5933 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| f2a3ff0e-88b9-366b-b81b-ddc5404de1e5 | -19.49515 | -56.59721 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.5 |
| 10b354c6-f492-3ee1-a70b-99cfa000e8df | -19.49375 | -56.62798 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 17093f67-3423-3c46-a114-6511d27ef47d | -19.4856 | -56.62096 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 7c33fc66-1b83-30f8-be16-5f010a2ef194 | -19.4836 | -56.6309 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 731207a0-3e25-31dc-afec-04c6fedb54b2 | -19.50726 | -56.58445 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 6ac09c9a-2fa4-3af4-a6c3-e6a31421b8c1 | -19.50566 | -56.56863 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f2ab2ac9-32f6-33e4-a13c-17123ba92293 | -19.50467 | -56.57356 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| dca599d2-6324-36cd-aed6-252cdc9c7292 | -19.5017 | -56.58838 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| c4d7815a-c9f8-30a5-b579-1ee066e76524 | -19.49873 | -56.60318 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.5 |
| 3bd67a63-ffcd-302b-9fa3-a88c0a4874af | -19.49833 | -56.62901 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 37e4462a-d819-3c83-a7ab-44dbb3ef66c3 | -19.49475 | -56.623 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| db8496b1-ee3f-37d0-a08f-91de32721947 | -19.49158 | -56.59125 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 85ae36b3-6bf5-3d74-82a7-08d04f3558da | -19.58947 | -56.61998 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| d947c3ec-d82c-3610-84df-95e438c5afee | -19.57855 | -56.72163 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 8f59b2f5-4eee-3c36-bcda-56bfc080485d | -19.57699 | -56.70555 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 0be34123-0048-3f85-8191-c67e89d6454b | -19.57497 | -56.71558 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| fbd1471f-1ab6-3e8a-9321-28abd2b32760 | -19.57341 | -56.69952 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 844797a8-c361-31c8-9d3d-8d4ffb7628e5 | -19.56641 | -56.69654 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| bda839ca-0dd0-3c58-adde-bec0b07d323c | -19.56543 | -56.70156 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 4122b1fd-ec5d-3da4-8451-6d4bfa32889b | -19.63049 | -56.70198 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 7b9c649a-c657-3d14-b8d7-492457c50b1a | -19.62292 | -56.71595 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| a7c50230-7234-3e42-9f2a-913a6589f7d5 | -19.62192 | -56.72095 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 5149bc1d-4383-3fdd-a8dc-46a30148270f | -19.61932 | -56.7099 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| a6986639-46f3-3e3b-b004-2d4d9b720e7a | -19.61473 | -56.70886 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 77b12ab1-66e9-311f-9b5a-54023ee10e18 | -19.61174 | -56.72388 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 05738d87-05f2-3d3d-a56b-6085b820eec8 | -19.61114 | -56.70282 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2305a21b-03a0-364e-a087-b759c88f9afa | -19.61014 | -56.70782 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 6955a576-11b4-3c4f-ad17-69b68747e104 | -19.60555 | -56.70678 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 5c762bb7-1ff9-3c99-961a-eff49d26efa1 | -19.60096 | -56.70574 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 87036612-4147-3ca5-ba08-b3f1980ef358 | -19.59895 | -56.71576 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 199660d6-f441-3e5e-8b5f-42f2ad429c1d | -19.58875 | -56.7187 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.3 |
| fb1ea080-5266-3881-96b0-6a8c71bb0367 | -19.58774 | -56.72372 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.3 |
| fa7c0066-f46f-3a75-aa9b-2abcb6ba692d | -19.58618 | -56.70763 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 984190dd-3e33-3c86-8575-8a59accebc8c | -19.58158 | -56.7066 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 784f32e9-bdc9-3e86-8e28-808d30e7fccd | -19.58057 | -56.71161 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c5770eda-e9b1-34a2-8ede-40867b8f7d47 | -19.57956 | -56.71662 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 949be834-db2f-3524-aaf6-e479f588619b | -19.57598 | -56.71057 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 0b0ea7a6-383d-3bf3-8fc8-c115e4fa32cc | -19.5724 | -56.70452 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 4c40d4dd-0625-3321-9cdc-297c6d0833ac | -19.57138 | -56.70954 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 6b0f4449-cca4-3ee7-8824-33f10f5317be | -19.56422 | -56.69745 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 32349ca5-427c-3d20-8155-d72517edff79 | -19.56249 | -56.71663 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.1 |
| 66745b03-3f13-30fb-8285-4a6173c8aa91 | -19.56219 | -56.70746 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| f566643f-9b23-3f3f-bb51-14de5b61d183 | -19.56118 | -56.71247 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| edbb0515-054e-3731-a51f-966dbb83a022 | -19.62751 | -56.71699 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 0156ee15-9575-3eb3-a9ee-c88c13d7f360 | -19.62652 | -56.722 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 2fceb2d6-23bf-3c0c-addf-6c9473a9fff4 | -19.6259 | -56.70093 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 62f6f941-5bc1-340b-8e72-e7c176d9ce33 | -19.61673 | -56.69886 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 1c650ca5-dc48-3884-a1d1-a213556b850d | -19.61274 | -56.71887 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| f70032e5-f83a-3963-b53f-d7096cf51ab6 | -19.60914 | -56.71282 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 453588ef-7682-3848-b09f-aab88f73f529 | -19.60814 | -56.71783 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 3f3453c9-dcd3-399b-80fd-732839f9a0ab | -19.60755 | -56.69678 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 0813bc59-ec30-39cf-8e26-4d6cfa261feb | -19.60455 | -56.71178 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| b0522d94-fe4f-3b66-b6a2-0205a199ee4a | -19.59995 | -56.71075 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 912b3226-9cc6-3dd3-abd2-92889a312e2d | -19.59737 | -56.69971 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 831b1da0-b1f8-3880-bcf7-0df298b8e3f8 | -19.59637 | -56.70471 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bc694c1f-b856-3e09-a2ec-f808dc129922 | -19.59335 | -56.71974 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.3 |
| d76a2bb4-d62b-367d-821a-51d63305ccda | -19.59077 | -56.70868 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |


[Clique aqui para ver as próximas entradas](README28.md)

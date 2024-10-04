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

## Dados Diários - Página 175

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51bb8b6d-64da-3f6d-be4c-969380791758 | -19.48458 | -42.89771 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| cef70976-d0da-3e53-acbe-7565b1956c85 | -19.48422 | -42.86534 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 46889b91-e90c-3caa-9b7d-1bfdbb110c8f | -19.48405 | -42.9041 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| dfff77da-51d5-338e-b422-849f5342e80a | -19.4837 | -42.87218 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| d5b82198-b60a-33c2-a7bc-2b9bfbe32771 | -19.48346 | -42.91132 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 69bc6e8c-24ec-3ae5-bfee-a1b0b506c1e1 | -19.48299 | -42.88159 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| d5997a90-7fea-340f-b8cf-3d45b1224156 | -19.48288 | -42.9184 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ef8a4983-bea8-398e-961b-82124fd8e37e | -19.48252 | -42.88776 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 184.0 |
| 6fa283fd-d78b-3b52-bc7e-ac1614e3dd39 | -19.48224 | -42.92611 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1f47981b-0aa8-3b24-b37c-f2708857f5ae | -19.48211 | -42.89316 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 184.0 |
| 743cc99c-b3f3-343d-ae33-62be38be1125 | -19.48168 | -42.93288 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e732e5e1-3ed1-3332-9ec4-8882297f1ea5 | -19.48166 | -42.899 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 47.1 |
| f707621a-242d-399d-801f-d9eb0c6af3fc | -19.4812 | -42.93878 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fa621d0d-96c3-34b4-90dd-6dd7ed3f00dc | -19.48118 | -42.90539 | 2024-10-04 04:59:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 47.1 |
| 33d55419-0b3d-36ff-a340-155a3963ab92 | -19.48068 | -42.91195 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5e3ace54-861a-3b00-a0fd-cc73be1132de | -19.48017 | -42.91866 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3c519664-eb13-3888-9816-342f3ab072fe | -19.47956 | -42.92665 | 2024-10-04 04:59:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 287de248-ec9c-3c49-bb3c-b39393971773 | -19.28773 | -43.77628 | 2024-10-04 04:59:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 458434db-c5b5-3531-9588-6911e185a499 | -19.28723 | -43.78257 | 2024-10-04 04:59:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e808a1b3-ab99-31fe-81bd-8a2c27428879 | -19.28505 | -43.77901 | 2024-10-04 04:59:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3cc0bf8e-b3f3-3b42-a087-ba97518db2a5 | -19.28152 | -43.76899 | 2024-10-04 04:59:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d957c1b8-b76a-38c5-9475-e06c86f55e8e | -19.28052 | -43.78145 | 2024-10-04 04:59:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2afe127a-f0c0-329c-bf4f-fe694866549b | -19.27888 | -43.77172 | 2024-10-04 04:59:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07dde38d-9339-3167-8680-bf4b26bb3bbf | -19.24628 | -43.75517 | 2024-10-04 04:59:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cec97392-cfbb-3201-88b8-85bb4df167bc | -19.06244 | -44.44307 | 2024-10-04 04:59:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 572232e2-b153-37a8-8d19-157ceb324ce3 | -19.06223 | -44.44209 | 2024-10-04 04:59:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e06281cc-80e8-31e2-a6e5-86154a936282 | -19.06195 | -44.44868 | 2024-10-04 04:59:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1ea1ebe-a9b6-3a02-9682-141c848caecb | -19.06171 | -44.4476 | 2024-10-04 04:59:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c9076d6-16c7-31a5-b807-e028052a8b06 | -19.23518 | -43.38149 | 2024-10-04 04:59:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf2f2158-fcf6-385c-8199-59dbe574d559 | -19.23502 | -43.3889 | 2024-10-04 04:59:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d90e386b-d0d1-3336-a557-7e4bd01a540d | -18.84981 | -43.57737 | 2024-10-04 04:59:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c511ec28-106e-37f3-8246-94f9f239f40b | -18.86229 | -43.59145 | 2024-10-04 04:59:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| d7b51ed5-c078-370d-95ef-806a1aaa85d0 | -18.85491 | -43.59769 | 2024-10-04 04:59:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 705781b2-53c7-3f8c-825c-477cd97a7da6 | -18.85551 | -43.59072 | 2024-10-04 04:59:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| eb52e29a-d1a4-3da7-b91a-d1edd1ad1ab5 | -18.854 | -43.60829 | 2024-10-04 04:59:00 | NOAA-20 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| b2c1d380-2432-32ce-9fa1-84367f797948 | -18.8489 | -43.58799 | 2024-10-04 04:59:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c48e3c04-1a5b-3240-b1f3-c15dd40176ae | -18.86175 | -43.5977 | 2024-10-04 04:59:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 76d90f51-fb52-3ec0-b154-d49073109430 | -18.8544 | -43.60363 | 2024-10-04 04:59:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| e2b8c54a-fd85-3974-8590-77a1f9e6481e | -18.84818 | -43.59637 | 2024-10-04 04:59:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 571e86da-e2c7-3f8b-877a-0156a5da21c8 | -19.2355 | -43.38294 | 2024-10-04 04:59:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 342b80c6-aaf7-3ba9-bf78-0f3da06813f5 | -19.23467 | -43.38742 | 2024-10-04 04:59:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52ce4269-9b37-3bef-a51b-f665bc79d9ed | -20.51848 | -44.89605 | 2024-10-04 04:59:00 | NOAA-20 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| aecf3494-0c48-3109-86a0-847fece6ed24 | -20.51797 | -44.90214 | 2024-10-04 04:59:00 | NOAA-20 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4cfe6771-c8e8-3adf-b811-27eac1e244d2 | -20.51746 | -44.90812 | 2024-10-04 04:59:00 | NOAA-20 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ff4facff-eb58-3beb-90b1-90b8b17f84a1 | -20.13745 | -43.8624 | 2024-10-04 04:59:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1a7211c3-d980-3795-88c2-5911e357f06c | -20.13118 | -43.85538 | 2024-10-04 04:59:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 80d56e8d-2687-3311-9846-7613a67daab3 | -20.12818 | -43.53186 | 2024-10-04 04:59:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 2e12c248-b6d4-3c5d-891d-0d62a925713c | -20.00876 | -44.49281 | 2024-10-04 04:59:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b762cecb-4803-33e7-9e2b-05a4f2e57751 | -20.00823 | -44.49912 | 2024-10-04 04:59:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| f9829133-a6e4-3b65-ac97-8dee8f27e013 | -20.00223 | -44.49232 | 2024-10-04 04:59:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3ad4e280-6988-3adc-b557-94a8fb8ab35d | -20.12906 | -43.52091 | 2024-10-04 04:59:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| b2fba333-2b37-3721-965c-22e533cb8ee3 | -20.10711 | -43.53501 | 2024-10-04 04:59:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 79437647-55bb-3d53-ba19-a99258f33529 | -20.12864 | -43.52609 | 2024-10-04 04:59:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 4aca7d70-5381-3fa3-b2c3-87f988eb8ccb | -20.10845 | -43.51805 | 2024-10-04 04:59:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a6b5b19c-3acc-3f8f-9815-8bea24ff79f2 | -20.10782 | -43.52603 | 2024-10-04 04:59:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b13459d9-b470-3063-afd5-b990faa3c736 | -19.98035 | -43.54829 | 2024-10-04 04:59:00 | NOAA-20 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4dd4f0ff-b4b3-3539-bd30-7cd3b981f580 | -20.50913 | -46.38297 | 2024-10-04 04:59:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7ef67c62-8c35-3564-8846-1f415be1b9aa | -20.50876 | -46.38689 | 2024-10-04 04:59:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 33f5f32b-4f42-35b0-9033-5e99772bc694 | -20.31162 | -46.8604 | 2024-10-04 04:59:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4e740205-b905-39c2-bec6-ff8b1bb54e34 | -20.31124 | -46.86441 | 2024-10-04 04:59:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c57cb4b5-aa1c-3fae-a91d-7b11b2687888 | -20.19164 | -47.46252 | 2024-10-04 04:59:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ea544ea7-7781-3cb1-b712-35706618f477 | -20.19132 | -47.46563 | 2024-10-04 04:59:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6c55c410-a6bf-30b1-a35d-ce499fc0e1f0 | -20.19101 | -47.46868 | 2024-10-04 04:59:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af75eaac-ae96-3bb2-8830-9db54f5927b9 | -19.53893 | -48.65118 | 2024-10-04 04:59:00 | NOAA-20 | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8b20a5fb-b77d-39e8-9434-c83a62896545 | -19.53459 | -48.64462 | 2024-10-04 04:59:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 61856a50-2c9a-3685-bf17-429b3e4e79e7 | -20.5175 | -48.75208 | 2024-10-04 04:59:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9172767c-3f0a-34e7-9b51-5c1f0aa76a79 | -20.51692 | -48.75255 | 2024-10-04 04:59:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e6b03a60-c2e9-3c32-a39e-e9b852b23c4e | -20.51723 | -48.74956 | 2024-10-04 04:59:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1b26f747-161d-3d7f-a291-d6b52ce07ecb | -20.51281 | -48.74844 | 2024-10-04 04:59:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 00c04370-be8e-3022-ab7d-2637551be7b5 | -20.51249 | -48.75139 | 2024-10-04 04:59:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2f3ef6ea-4b3c-3014-a89c-15b4a75e8367 | -20.5081 | -48.745 | 2024-10-04 04:59:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 44219e8e-9fae-37a3-b455-4a6995a08303 | -20.50695 | -48.75547 | 2024-10-04 04:59:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 05a4e476-0bac-3515-9e6b-a7094f00651e | -19.53959 | -48.64524 | 2024-10-04 04:59:00 | NOAA-20 | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 15f5b8c5-59e5-3c40-9d1e-0ba7af02de5f | -20.51783 | -48.74909 | 2024-10-04 04:59:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1515bdd5-1397-3043-9e74-ad3f1cd8e1f0 | -20.50744 | -48.75098 | 2024-10-04 04:59:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 70c49686-1285-3ec7-8bbc-a809c860c286 | -20.50777 | -48.74799 | 2024-10-04 04:59:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| d608c422-f651-336b-a638-a4ec0e90e473 | -18.716 | -57.32093 | 2024-10-04 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| dc679cf6-ede0-34d5-a3b8-51a6203d3194 | -18.69785 | -57.30653 | 2024-10-04 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 442705e0-512d-3d45-9588-ef9f22b96d4f | -18.69627 | -57.29504 | 2024-10-04 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5ca02a58-6d26-36a3-96d6-2c344d2a22c1 | -18.69512 | -57.30231 | 2024-10-04 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| eb79081a-627d-31e2-900c-2bbaba853ce6 | -18.69353 | -57.29082 | 2024-10-04 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 9f3d10a5-831b-3ca9-84c4-ccbb3ccb34df | -18.69296 | -57.29446 | 2024-10-04 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 86029d4a-a703-3b69-8fec-7742322981d6 | -18.68502 | -57.32298 | 2024-10-04 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5097d77c-e8e0-3125-9533-515b82a82c13 | -18.88563 | -57.70637 | 2024-10-04 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 22891e58-3ef7-3706-9c14-eedd5bf1e305 | -19.74763 | -54.05738 | 2024-10-04 04:59:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 67fd17be-3f3e-3345-84ef-083cf566621e | -18.05052 | -53.8722 | 2024-10-04 04:59:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 69d8aa4f-d5c5-34e6-8162-af463c960cb4 | -18.30982 | -54.25177 | 2024-10-04 04:59:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9283086e-088b-3240-81b0-51178b057c38 | -19.58278 | -56.53116 | 2024-10-04 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 6c111a31-b6a8-332d-8af2-65c7becea26a | -19.58611 | -56.53173 | 2024-10-04 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 81cc31b2-c3a4-3712-8dfd-30a23eec0852 | -19.57946 | -56.5306 | 2024-10-04 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 1d799da3-1453-3dd9-8e22-854004770d81 | -19.57557 | -56.53371 | 2024-10-04 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 7f788bf8-eb7f-3b7d-a2bf-59f1f050cfea | -18.89225 | -57.70337 | 2024-10-04 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 020c7979-6d29-3027-b35f-af0fed4a3040 | -18.68849 | -57.30116 | 2024-10-04 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 64611440-2069-3ff5-976a-2ce4bc914cb2 | -18.71327 | -57.31671 | 2024-10-04 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| dd642ca1-1432-3b8c-9e66-1070c32f15d0 | -17.20144 | -57.35899 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 349441ee-130f-3eac-a923-92ecf73af9a1 | -17.19811 | -57.35841 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 9b5f81fc-2072-3a17-bc23-0208be2d98cc | -17.19479 | -57.35783 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 5c1ddc59-adb9-3e6a-bae7-efd0db1e9648 | -17.19421 | -57.36147 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| b68b433c-9bd5-38f3-8f4f-f9c8bcff32d4 | -17.19362 | -57.36509 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| ea707b10-099e-3613-9c06-71446da41860 | -17.19205 | -57.35361 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |


[Clique aqui para ver as próximas entradas](README176.md)

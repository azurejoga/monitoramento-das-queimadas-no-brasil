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
| 627d879a-ff34-382d-82e4-b8a5e8f3fb01 | -12.56637 | -43.07839 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 47a63de3-af38-39f4-9dbc-909df50331f5 | -16.90159 | -42.10378 | 2026-10-02 04:17:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 83ee8fcb-62f3-3765-9316-adaf523b776a | -13.39614 | -46.82606 | 2026-10-02 04:17:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca240034-8366-3f85-84e7-c8cb65951a7a | -11.4632 | -43.5188 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2caa9335-88da-3bbb-be82-8b8a118e1362 | -11.73296 | -43.44757 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21c2f645-8ad5-3788-b4ad-9da671e68550 | -16.85592 | -40.58138 | 2026-10-02 04:17:00 | NOAA-20 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fdfb46bd-bc3c-35e8-bfdf-dffdb88593b8 | -10.30106 | -44.64239 | 2026-10-02 04:17:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0488e6e0-eb64-3a3c-b092-f9dac4b2f5f2 | -11.64836 | -43.57135 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 914068d4-e633-32b9-ae49-a0c7ebf34e4a | -10.251 | -49.67744 | 2026-10-02 04:17:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34c595da-0d4e-3911-b4d1-c5454e80f057 | -11.7374 | -43.44106 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8bb4a51-20b3-3c95-a0e0-e8e9717be5f6 | -16.86062 | -40.5795 | 2026-10-02 04:17:00 | NOAA-20 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 322cbf78-b7c8-356a-b448-006761dcb688 | -11.62384 | -43.57835 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0292448d-f020-362d-9c71-1e3bd2602a30 | -10.25271 | -49.66783 | 2026-10-02 04:17:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6c374f36-b73c-3700-97cb-ca2e864a5b49 | -11.75007 | -43.57327 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 2b501ef1-81f4-3bcf-ae44-b302bcabf6a2 | -11.66706 | -43.60349 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8761682e-91e8-3b88-90f6-4452f058088e | -12.99121 | -51.27608 | 2026-10-02 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 49294069-7916-3d38-8e23-c377d36ea927 | -14.2053 | -43.62403 | 2026-10-02 04:17:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea27c8db-4241-35d9-958f-4afce3aeab9a | -14.77767 | -40.33292 | 2026-10-02 04:17:00 | NOAA-20 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d784e7f0-d09f-35b7-9d1b-b80acb9cbc0a | -11.64732 | -43.55667 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4bedec01-313d-38b0-a4b1-91716eec84c2 | -11.74679 | -43.44623 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23b634fa-2c96-3fc3-9aaa-44caba900762 | -11.13228 | -44.62348 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f4bf690-707a-3e1e-83c1-0c812d5a9c96 | -11.68148 | -43.59862 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f703406-1f5b-3498-814c-59abd785ec19 | -12.66589 | -45.09368 | 2026-10-02 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc0e643c-ebe2-3101-a6e6-ee6b775498ce | -18.33451 | -40.05914 | 2026-10-02 04:17:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bd9d4d1a-7281-352d-9102-87c3fca667db | -11.46297 | -43.43544 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5156a449-8b55-377d-abd5-7ebbd2957e71 | -11.26874 | -43.56651 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b68870a-1260-3cdb-a366-1ba11070edde | -11.15831 | -44.61612 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 925becb8-f0d2-3f64-80bb-74b5cbef1a1d | -11.74894 | -43.58031 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| fc0e5d09-37d3-3105-bbe0-e4859fa3a6aa | -11.34463 | -43.34734 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67ec5d82-31b5-3aec-8b76-68dc7c121789 | -15.77463 | -46.03162 | 2026-10-02 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 195272a2-d37a-3d11-86b2-3586af455fb1 | -10.21528 | -45.31119 | 2026-10-02 04:17:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d47a6bd-9a98-35fc-b27d-2731aa443e77 | -15.30798 | -42.78207 | 2026-10-02 04:17:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d80f878b-7071-395b-a2b2-a1afc32fb178 | -17.21576 | -41.2067 | 2026-10-02 04:17:00 | NOAA-20 | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| d7acc24b-5102-3e8d-8201-91ab366a779c | -13.86355 | -43.63645 | 2026-10-02 04:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cf05cae3-dea5-3672-8b5b-5fcee103d38f | -10.90485 | -43.84327 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa389c3c-3db9-3981-887a-657fd1e9c493 | -10.8256 | -51.09933 | 2026-10-02 04:17:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3ee8798c-2eea-39a1-af7b-6dcc589559c6 | -11.24896 | -45.2187 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d952155-04f9-3b96-b462-c16b4eedb363 | -11.22754 | -45.17522 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af025e9f-1b8a-30d6-9bb9-985b58bbb1e1 | -11.76725 | -43.57246 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81595c7b-a7fd-3352-a413-f416977895b5 | -15.63483 | -43.23392 | 2026-10-02 04:17:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3fadc490-15a7-32df-b80d-59f77e605e53 | -11.7534 | -43.57382 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| e72e493a-0df8-33aa-bb21-6e46940533a0 | -11.69591 | -43.59374 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 765bff78-6355-3f92-a357-9fbe3107a68c | -13.35726 | -38.97485 | 2026-10-02 04:17:00 | NOAA-20 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 34c13bbb-472e-3c56-9123-d9d807fdf350 | -12.55975 | -43.0773 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f1dc41b8-27e4-33e4-8f79-fe19aa9c132b | -15.11632 | -43.61803 | 2026-10-02 04:17:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 77d54247-4dca-3a2d-9886-9fbf1700e8a9 | -11.24739 | -45.20657 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1aa307d2-4b5f-3e20-b677-d8673bff71b8 | -11.1307 | -44.61166 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 095f35ad-35be-3121-9660-55f66f3158a9 | -11.76734 | -43.55073 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07205c07-862b-3bfc-bfbb-5dfb2e834206 | -13.79996 | -45.26042 | 2026-10-02 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af3c4a7c-74d4-3c79-985a-ca800ca09b42 | -11.45973 | -43.41319 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6543c6ea-1074-3e99-873f-b18902002e54 | -11.24862 | -45.23011 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d360a1b3-63e3-3731-b3b0-14cbb823e26e | -11.15212 | -44.61123 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| fc8e7229-8153-33dd-b42f-0c6092b4968d | -13.13661 | -40.87355 | 2026-10-02 04:17:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c63391cf-5207-37b5-9f10-6729a467f4ae | -16.12145 | -42.2244 | 2026-10-02 04:17:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6c5ecea5-4258-306e-b1aa-67a9553d485e | -10.26358 | -49.65789 | 2026-10-02 04:17:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 0ae973ae-7402-3337-bd97-111dbd1ec241 | -11.40538 | -43.3718 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 917a62ea-431c-3478-8e78-eaae399fa98a | -11.26485 | -43.56951 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1cbb00dc-a146-3b33-a624-1443a44d258c | -13.78543 | -45.24245 | 2026-10-02 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 39a6ae35-0935-3c53-a817-cacf9f6d04fc | -11.13654 | -44.59731 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d6af9e2-ac0c-3d49-812c-2aaab0e87c14 | -12.92316 | -42.4474 | 2026-10-02 04:17:00 | NOAA-20 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 94eb7e0d-9609-3dfc-b2ec-57df8ed0f302 | -16.11805 | -42.22383 | 2026-10-02 04:17:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5cca82de-7764-343d-8126-ada683e0f474 | -11.71807 | -43.43425 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1be3d5f4-e056-32d8-bba9-3a759c5693a4 | -10.80723 | -49.33979 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ef1e4c47-7daf-3fc2-9f25-eccaccbf10ba | -10.61036 | -48.05118 | 2026-10-02 04:17:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d7ff5d5-2860-34bd-b836-f56721a55cee | -11.74622 | -43.44976 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac62b206-85d2-35bf-b88b-b515fbb909a8 | -10.24572 | -46.63196 | 2026-10-02 04:17:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ef151d2-b710-370e-9222-4f27331503e5 | -11.26164 | -44.26226 | 2026-10-02 04:17:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6c81858-e605-30ca-8611-0ee6c45ba07f | -11.47349 | -43.43356 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f64fdeaf-5808-3b2f-b652-0bdad5a126bf | -11.78054 | -43.57456 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 980773fe-b2ac-3835-8033-107957b4c0d7 | -11.73627 | -43.44812 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4dc02fdf-44e9-3e8b-84ed-176ae0dc8418 | -10.30261 | -44.65439 | 2026-10-02 04:17:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 896d3de3-6ce0-35b0-a729-5700151317b7 | -13.49072 | -42.50945 | 2026-10-02 04:17:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 472f4beb-9ba4-3d12-876a-ddb9a4397773 | -12.51831 | -43.10303 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 682ca17f-cf73-3ec7-a4ce-2017631362a6 | -13.86574 | -43.64408 | 2026-10-02 04:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 75da74e2-e1dd-349a-9f71-1295308ba735 | -11.24454 | -45.20212 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 70f38f70-8d05-36dc-9d5b-13fca716ceae | -13.39279 | -44.00969 | 2026-10-02 04:17:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 667b183b-45ec-3622-a237-9049887e0a03 | -10.91211 | -43.84082 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2165c7f4-a9ee-38e2-8cd0-77604d38d709 | -12.19099 | -47.11361 | 2026-10-02 04:17:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 524c417e-a132-393b-8cf0-c9674f423950 | -11.40813 | -43.37587 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a81e53de-6c8a-3a18-b7e7-10397fc7db72 | -11.70061 | -43.52194 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 351fb96c-5cae-3a28-be00-795b3a40ff5d | -11.46078 | -43.42785 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b8187193-c4ed-3fa7-bb3f-afc3903fb890 | -15.47985 | -40.76746 | 2026-10-02 04:17:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c19b8860-ec69-3f4d-bc46-3821fc441f62 | -12.9888 | -51.27623 | 2026-10-02 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 15014cd1-4717-34bc-89c1-902e41444b86 | -11.45642 | -43.41264 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| acfa3a49-e8af-3ffd-9cee-3c4b50ab4595 | -13.7935 | -45.23607 | 2026-10-02 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b9ff1a7-8b25-3a5f-88ad-c8a4c018e890 | -11.72279 | -43.5111 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f6423c3b-845c-39c7-9025-36453f42c450 | -15.11963 | -43.61859 | 2026-10-02 04:17:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2ff81d12-8855-308b-badf-6feae60a9106 | -13.33428 | -43.86466 | 2026-10-02 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5467c0ae-6df1-3b00-b803-fbdb1a118fd1 | -11.84515 | -44.74939 | 2026-10-02 04:17:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc4da6b7-fb91-331b-9b7a-7d6a0cfaa79f | -11.78224 | -43.56404 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25c7ed5d-1d53-3b55-b998-2d3cc30a6b5d | -16.13905 | -43.74427 | 2026-10-02 04:17:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc661dcb-e959-3ed8-b956-940dafe9d97b | -10.24727 | -49.67175 | 2026-10-02 04:17:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0881f832-e44b-395d-98ec-ecba9f4188a9 | -12.5288 | -43.10114 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ed21fcfd-e31b-3d46-b96e-eccd8808b1ec | -11.65709 | -43.60186 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 35.9 |
| ab117b6c-3fc6-39ea-ae8b-c85458802e1e | -11.4713 | -43.42596 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a7411ea9-19df-36a4-ad76-a73e5b88e507 | -11.75463 | -43.545 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f64d339-0b0c-30e7-a9a1-fa0d1d32b2ae | -11.75406 | -43.54853 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63b5dc6d-30c6-3986-96aa-8a6541936514 | -11.7922 | -43.56562 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5a3fb78-f2ae-3e5e-ae9f-4239dc40b3e4 | -15.25436 | -46.17526 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 39b1217d-1c3e-3fcd-b9ba-ed20baaa2aeb | -11.66487 | -43.59588 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README44.md)

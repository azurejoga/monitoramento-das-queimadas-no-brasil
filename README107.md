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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c325fb9-ed8c-3239-ad01-2c3383e60430 | -8.2745 | -37.61142 | 2024-10-29 12:14:00 | TERRA_M-T | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 24ef05b0-c26b-317a-88ad-fc213ce7e8a5 | -7.49809 | -37.01842 | 2024-10-29 12:14:00 | TERRA_M-T | SUMÉ | PARAÍBA | Brasil | 2516300 | 25 | 33 | nan | nan | nan | Caatinga | 45.5 |
| 2247a849-f333-3abd-9ffc-95c1e2fd3665 | -11.138 | -55.5313 | 2024-10-29 12:16:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 265.5 |
| 4a2cf07c-6a6d-3b8c-b3aa-5b43a38f5454 | -11.1378 | -55.5515 | 2024-10-29 12:16:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 201.9 |
| 8a7f4046-ac8f-303c-847f-9edb488f2d75 | -13.6222 | -45.5838 | 2024-10-29 12:16:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 158.4 |
| 64d9babc-433d-31e7-993e-c1869c229164 | -11.69127 | -47.10175 | 2024-10-29 12:17:00 | TERRA_M-T | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| e97f804b-6747-30f7-9986-f2b5df2cca40 | -10.11824 | -46.50753 | 2024-10-29 12:17:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| db278302-324b-30d1-b497-fd658408aaf3 | -10.12258 | -46.5202 | 2024-10-29 12:17:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 37c0b9b4-65f3-3711-a472-8966fd67a921 | -10.1253 | -46.50288 | 2024-10-29 12:17:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| c17ae862-e605-3119-974b-b2e5b23b20a4 | -10.13023 | -46.50959 | 2024-10-29 12:17:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 5f907671-e194-3ff9-bf47-8f2bca34dcc7 | -13.88002 | -45.21107 | 2024-10-29 12:17:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 182c3d87-17cc-33e1-83bb-4340152ece6e | -14.00806 | -46.13713 | 2024-10-29 12:17:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8062e8df-c891-3dc7-8ca4-c91eda1e38c3 | -12.70119 | -45.86737 | 2024-10-29 12:17:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 89b048de-9109-3916-8645-267ecbb0e3f4 | -13.62532 | -45.58326 | 2024-10-29 12:17:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 6f99f5bd-8e4a-3102-8c2e-ce31391358c9 | -13.63581 | -45.58499 | 2024-10-29 12:17:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 54272eb4-4858-3e86-b949-b291f7c9bcd9 | -13.69946 | -45.4962 | 2024-10-29 12:17:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 6e1d711c-0c85-3eee-b211-906b9f5f85c1 | -13.70987 | -45.49791 | 2024-10-29 12:17:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 183942c3-1271-3b37-adde-13e20154a645 | -13.71195 | -45.48513 | 2024-10-29 12:17:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6a143f27-b6ad-3f1a-b51e-7ae2faddfb94 | -11.11625 | -46.04882 | 2024-10-29 12:17:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 488a6e07-eba5-3fbc-ab44-00f51997b4a5 | -11.11805 | -46.04319 | 2024-10-29 12:17:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 9a3936e3-46d1-38ae-941f-667fb565d651 | -11.11874 | -46.03367 | 2024-10-29 12:17:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 0f05880e-b589-3a6a-939c-0f2bbd710447 | -11.33509 | -45.03394 | 2024-10-29 12:17:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| d42e6ea7-8fac-3030-84a5-ad9dfbaa53ed | -13.77629 | -44.36055 | 2024-10-29 12:17:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| db2e96f2-33d0-3a2f-8ca6-0cb4967f6019 | -13.7803 | -44.35593 | 2024-10-29 12:17:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| f32dfb59-d600-39a4-affb-dce7066f8db6 | -13.85778 | -43.98708 | 2024-10-29 12:17:00 | TERRA_M-T | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a560695f-2f2e-301a-a17e-abd11162c6fc | -13.88935 | -43.97078 | 2024-10-29 12:17:00 | TERRA_M-T | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 27.9 |
| d66d9c01-9254-3954-9f47-96fbefda60e4 | -13.90983 | -43.96339 | 2024-10-29 12:17:00 | TERRA_M-T | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 64172c49-1933-3c56-a968-a508196580f1 | -13.91141 | -43.95302 | 2024-10-29 12:17:00 | TERRA_M-T | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 39.7 |
| c9a75588-3e7e-3084-823d-9fabd99497b4 | -14.14076 | -44.07264 | 2024-10-29 12:17:00 | TERRA_M-T | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 51d16457-5ea1-3587-8af6-6f60801e68e7 | -14.15023 | -44.07417 | 2024-10-29 12:17:00 | TERRA_M-T | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 835559bc-92dd-3aac-aed4-63da2bbbe06f | -14.19447 | -43.72399 | 2024-10-29 12:17:00 | TERRA_M-T | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 8221829e-f2ca-3019-bd74-db7fc1dc5d4b | -12.59689 | -44.10146 | 2024-10-29 12:17:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 08fae2ba-4c8b-371c-ae64-9452a3db578d | -12.66331 | -43.82434 | 2024-10-29 12:17:00 | TERRA_M-T | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| f21a3e18-807b-3007-9745-bddde515c1a3 | -12.75389 | -43.89848 | 2024-10-29 12:17:00 | TERRA_M-T | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| fde1828a-844d-3002-90e1-d0f68ec7a81f | -12.87773 | -44.60766 | 2024-10-29 12:17:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ceca33b0-3ed1-335a-961a-c0d518ac087b | -12.88588 | -44.62079 | 2024-10-29 12:17:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 420.5 |
| 8ec2a151-9b91-37d9-a21e-948bc14ecd34 | -12.88767 | -44.60923 | 2024-10-29 12:17:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 218.3 |
| 639e6065-6fd6-3e56-a401-fcb3a9825943 | -11.53902 | -43.99149 | 2024-10-29 12:17:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 9833bbb4-2597-3ac0-96bc-82d461ae7c60 | -11.55048 | -43.98201 | 2024-10-29 12:17:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 238790af-7f19-35fb-9e03-c41709ec617d | -12.14911 | -44.07791 | 2024-10-29 12:17:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| b17f76dc-408a-36a8-bba8-5f50fce4798f | -15.44372 | -43.64691 | 2024-10-29 12:17:00 | TERRA_M-T | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 37.5 |
| 92bc60d3-264b-3f6d-848e-8ac36db5c7c8 | -15.4452 | -43.63711 | 2024-10-29 12:17:00 | TERRA_M-T | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 031739b5-b0a5-36b4-be29-710f34cb6e86 | -15.55359 | -43.82848 | 2024-10-29 12:17:00 | TERRA_M-T | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 16.2 |
| d7ba3ae3-fd22-348b-af61-2340f6995633 | -14.33966 | -43.37761 | 2024-10-29 12:17:00 | TERRA_M-T | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 56ce5f2c-178d-3502-bceb-0c2cff79ed84 | -14.34114 | -43.36789 | 2024-10-29 12:17:00 | TERRA_M-T | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 7984196c-7146-3309-b450-1f9939857f81 | -13.69458 | -43.12476 | 2024-10-29 12:17:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| ab6921af-bab6-35f5-a855-ea63009e1f70 | -13.8482 | -42.84265 | 2024-10-29 12:17:00 | TERRA_M-T | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 7ae0536d-06f1-3db1-bf47-5ee1df38bd08 | -13.90172 | -42.79302 | 2024-10-29 12:17:00 | TERRA_M-T | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 17.9 |
| bb2c8dd1-97cb-3318-ad53-d4f57d8f91cb | -13.90309 | -42.78382 | 2024-10-29 12:17:00 | TERRA_M-T | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 11.8 |
| e51ea06d-0cb4-36c1-bd0a-4b85f0a246d4 | -14.17512 | -43.12225 | 2024-10-29 12:17:00 | TERRA_M-T | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 16.4 |
| da1c2b6a-d32d-3e51-a4a0-3dccf0f984ea | -14.28632 | -42.8742 | 2024-10-29 12:17:00 | TERRA_M-T | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 47d81c8f-2a0e-30f9-8bd5-29701aaa4cac | -14.28774 | -42.86482 | 2024-10-29 12:17:00 | TERRA_M-T | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 34.6 |
| d972dc82-3f48-33ae-9280-50dd263028e4 | -15.0952 | -43.62348 | 2024-10-29 12:17:00 | TERRA_M-T | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 700c3dda-00f5-3fe4-9a64-39b80d07ff05 | -12.60485 | -42.33101 | 2024-10-29 12:17:00 | TERRA_M-T | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 28.3 |
| 79b34a30-d4d4-3726-84be-67a448dd7077 | -12.63979 | -42.1628 | 2024-10-29 12:17:00 | TERRA_M-T | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 7a5c2b83-27ad-3d13-9805-57e2de314253 | -12.68734 | -42.58466 | 2024-10-29 12:17:00 | TERRA_M-T | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| b030d72b-5925-38d6-a1b4-b5383daac9ce | -12.91175 | -42.31744 | 2024-10-29 12:17:00 | TERRA_M-T | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 46b9e14e-c3a5-3e31-83db-b19a6c250182 | -12.92753 | -42.27272 | 2024-10-29 12:17:00 | TERRA_M-T | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 17.5 |
| fbab46f4-4acb-3849-9a89-4eca4142842f | -12.92889 | -42.26352 | 2024-10-29 12:17:00 | TERRA_M-T | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 18.3 |
| ef2fbe0d-c32a-3113-b0e7-995a80cd8c0e | -12.98415 | -43.06382 | 2024-10-29 12:17:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 2325c2cf-f67c-3024-a03c-18c4d50c339f | -13.10975 | -42.47322 | 2024-10-29 12:17:00 | TERRA_M-T | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 3797d16d-4662-33fb-b176-a1fb7ca047e3 | -13.11112 | -42.46393 | 2024-10-29 12:17:00 | TERRA_M-T | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| c0ea5499-cad4-3211-b5bd-5dfdae653d5d | -13.42057 | -42.98852 | 2024-10-29 12:17:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 81c427fb-802d-3f09-aa6e-10b6a12cab7e | -13.42823 | -42.99952 | 2024-10-29 12:17:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 8c60c873-dc76-3273-8d7e-1a72011074ce | -13.42965 | -42.98996 | 2024-10-29 12:17:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 58.5 |
| 15d864ba-4630-3733-af96-fe1cbb135f7b | -13.4829 | -43.2515 | 2024-10-29 12:17:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 151.7 |
| 0fb3b316-4cf3-3c4a-b4f1-25885c700e47 | -13.48436 | -43.24174 | 2024-10-29 12:17:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 17.6 |
| a6328adc-4f88-3eb7-9241-c7b67083bbb7 | -13.49093 | -43.24933 | 2024-10-29 12:17:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 26.3 |
| cc0b53a7-f859-334c-a78a-5ce7532e65f2 | -13.60334 | -42.99993 | 2024-10-29 12:17:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 8b130fd5-0d78-3f52-a573-7efb36023e83 | -13.61384 | -42.3064 | 2024-10-29 12:17:00 | TERRA_M-T | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 70d44b84-f76e-32ac-97db-2494e937e7f3 | -13.63753 | -43.13902 | 2024-10-29 12:17:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| a9cbab34-db38-36c4-b9bc-7267b1a9602c | -13.63899 | -43.12937 | 2024-10-29 12:17:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 19dd2678-531f-3510-842e-485f46cf62b5 | -10.93838 | -42.43302 | 2024-10-29 12:17:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 469250fc-a178-3195-b89d-949062474fbb | -11.28577 | -41.96164 | 2024-10-29 12:17:00 | TERRA_M-T | PRESIDENTE DUTRA | BAHIA | Brasil | 2925600 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 64abedac-9736-39be-9b63-bdaa1e3426ef | -11.42735 | -41.55561 | 2024-10-29 12:17:00 | TERRA_M-T | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 096abdf3-9da0-3182-9d74-9ac6fd7dffa7 | -11.71345 | -41.68739 | 2024-10-29 12:17:00 | TERRA_M-T | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 336879b7-1782-3522-9013-a74fbd0367f2 | -10.28323 | -41.3777 | 2024-10-29 12:17:00 | TERRA_M-T | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 27.6 |
| 5464918e-3fcf-3ba6-842a-dc7128037b60 | -10.28455 | -41.36871 | 2024-10-29 12:17:00 | TERRA_M-T | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 8dc28cfe-4b5f-35f4-bce5-95dff772d640 | -13.93652 | -41.99168 | 2024-10-29 12:17:00 | TERRA_M-T | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 6b68b695-666e-3531-b138-e153f4a0583d | -13.95144 | -41.82687 | 2024-10-29 12:17:00 | TERRA_M-T | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 24.2 |
| e7a6b0b5-b376-32af-b64d-aa757842e14d | -13.95276 | -41.8178 | 2024-10-29 12:17:00 | TERRA_M-T | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 631145b0-f1b9-378a-ab61-97772f75c56d | -14.14528 | -41.63651 | 2024-10-29 12:17:00 | TERRA_M-T | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 8c1b4c41-eb35-3d0a-b3a7-34972865e23e | -14.27865 | -41.86358 | 2024-10-29 12:17:00 | TERRA_M-T | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 4fe5c5a5-2322-3e15-9edb-ea64ab933e17 | -14.59177 | -41.02748 | 2024-10-29 12:17:00 | TERRA_M-T | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 24.4 |
| cff81e6f-fb1c-3ad6-b7dd-f6a9ff3f5be8 | -14.59307 | -41.01824 | 2024-10-29 12:17:00 | TERRA_M-T | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 15.7 |
| c33533ea-2105-3db4-8df6-6490e2c66486 | -12.49434 | -41.64024 | 2024-10-29 12:17:00 | TERRA_M-T | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 1308a88b-4928-3572-af5c-bef66858a474 | -13.56758 | -40.77619 | 2024-10-29 12:17:00 | TERRA_M-T | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| cf222b3f-b967-3c0e-b2d2-c3e7ad600f6e | -10.46494 | -41.19942 | 2024-10-29 12:17:00 | TERRA_M-T | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| b97d206a-5886-3fbc-8f21-534c1ed7e252 | -10.64841 | -40.12265 | 2024-10-29 12:17:00 | TERRA_M-T | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | 37.9 |
| 9c70ee46-e882-3e45-833c-03a17d47946d | -10.6497 | -40.11353 | 2024-10-29 12:17:00 | TERRA_M-T | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 8b9d1d91-d0e6-3e46-b5d4-00537c6b1106 | -15.21942 | -39.95398 | 2024-10-29 12:17:00 | TERRA_M-T | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| b6aa2f78-5195-38e0-9baf-944d9020fdd3 | -15.22871 | -39.95531 | 2024-10-29 12:17:00 | TERRA_M-T | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 49.7 |
| dc844086-09af-3d5e-addd-7eac83501da4 | -15.23726 | -40.42612 | 2024-10-29 12:17:00 | TERRA_M-T | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 88a05e94-caeb-3a95-9af7-c9a05ecdfbfd | -15.24638 | -40.42742 | 2024-10-29 12:17:00 | TERRA_M-T | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| ce0e3289-3a79-33d5-ab7c-ccd2a5553047 | -15.42452 | -39.79773 | 2024-10-29 12:17:00 | TERRA_M-T | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| b5e44072-d26b-302c-a475-0ba9ebf90421 | -16.09094 | -40.44382 | 2024-10-29 12:17:00 | TERRA_M-T | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.0 |
| 5a3c1680-80f8-327c-b8cd-94f8a2945f2b | -16.20776 | -40.92799 | 2024-10-29 12:17:00 | TERRA_M-T | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| 6d0bd4c6-d83b-3bec-abd6-856199027630 | -14.30031 | -39.67063 | 2024-10-29 12:17:00 | TERRA_M-T | AURELINO LEAL | BAHIA | Brasil | 2902401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 46.4 |
| 0f3af4d1-11f9-3034-ab20-f01c12496bfd | -13.05763 | -40.34501 | 2024-10-29 12:17:00 | TERRA_M-T | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| d14607ca-dd93-3a9f-b134-4abb47af905f | -11.89152 | -39.33208 | 2024-10-29 12:17:00 | TERRA_M-T | RIACHÃO DO JACUÍPE | BAHIA | Brasil | 2926301 | 29 | 33 | nan | nan | nan | Caatinga | 24.9 |


[Clique aqui para ver as próximas entradas](README108.md)

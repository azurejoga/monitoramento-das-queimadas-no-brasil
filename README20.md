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
| 89070d9f-35ca-38d9-b9a2-4569f4daa9f1 | -13.08491 | -56.91575 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 9b6dab05-2653-30a8-bc69-22048a6e9ae2 | -12.71806 | -47.79388 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fcd4210d-dbb8-3b4d-b660-55be1d24816a | -12.68791 | -48.07669 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5bf6cf3-9171-3f09-84cc-653af1c87fe7 | -12.72277 | -46.39406 | 2025-08-05 04:19:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b307f43f-1c05-3438-801f-62a761a1acc4 | -13.03831 | -56.87597 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b59bee67-4641-3bd3-967d-8db1577c3d29 | -13.42754 | -47.46332 | 2025-08-05 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12dcfcef-39d7-3d88-97cb-48b5c1de3388 | -12.4435 | -48.71958 | 2025-08-05 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 752f9358-11f6-395d-970e-cbb5a42b8dac | -13.07664 | -56.89159 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3dc10704-7742-38f3-81f6-db507eb2196e | -13.22754 | -46.84481 | 2025-08-05 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ff583a5-cbd8-3a2d-96ac-c3e6ae0b4bce | -13.03899 | -56.91161 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23c87036-a0d7-37a0-af21-a724b566933f | -15.38767 | -40.84066 | 2025-08-05 04:19:00 | NPP-375D | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 889f5c56-4b7d-3b5d-b6be-72d3b42a6249 | -20.74562 | -49.40231 | 2025-08-05 04:19:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 51f3c430-ccd7-3081-be58-0af08ab63471 | -12.69207 | -48.11873 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dae05d1d-a2c9-3cf9-b391-de6b8dfdcc4e | -13.04444 | -56.91099 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| eabd33fd-c7c3-37bd-bba5-4d4fa470bb68 | -12.69901 | -48.07858 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f78d378c-d1ac-3c53-b9f5-9c8068931cc8 | -12.95074 | -48.25347 | 2025-08-05 04:19:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c9bc8b03-5409-35e7-b693-3536610dfa74 | -13.07549 | -56.88968 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d262e5d4-335c-36c5-9d42-bc4c481a7175 | -12.70941 | -48.08448 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 727a5b58-6aee-3e83-897f-55e963b19368 | -14.3501 | -47.10176 | 2025-08-05 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e0fb202-e37e-3f1a-80a9-fb2b445739c3 | -13.05871 | -56.88173 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5574709e-3c2f-3bfc-9ed7-cc01d8e61f7c | -13.06058 | -56.90439 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25f4abd6-4c19-3da2-9620-768de818db8d | -12.68315 | -48.12613 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23535d73-fa8b-3299-b7fd-3428f19b72ab | -12.71816 | -48.10003 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70c1c7a1-da0d-3979-b016-ac309e7d2b3e | -13.04705 | -56.87378 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 88655782-5a38-328e-9ae3-eb4909dfb34f | -13.05952 | -56.90253 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e22e16f9-1513-3683-95ba-75dedb3424f9 | -15.39148 | -40.84132 | 2025-08-05 04:19:00 | NPP-375D | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f09fe526-c647-3b90-9153-3db824fcb81f | -12.68393 | -48.12164 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 205a5633-dc49-34ef-8ebd-a2cb4d1a68c3 | -13.06508 | -56.88314 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1090218f-8ad8-3645-8673-a4e6c95d1392 | -13.0819 | -56.8983 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dfed6c12-143c-3960-9fc2-e8bb615cf17a | -12.72902 | -46.39895 | 2025-08-05 04:19:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 994c5b25-3907-33f2-9b47-ad28eb4b68ce | -13.0808 | -56.9035 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 64b328ae-1ce1-397c-9be3-0a98ad425e78 | -13.05416 | -56.90313 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1dac0f76-2dba-39ff-b996-5d206f35b21e | -12.69132 | -48.12306 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e7204da0-a8af-3a39-b8e1-f0ff3e7f5b28 | -13.05112 | -56.87846 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b560e7e1-a1fb-39d1-be69-14f9dd7e6fe4 | -13.24422 | -46.85181 | 2025-08-05 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8523cee5-cd49-3790-b0df-664dbf297b6f | -13.07023 | -56.88278 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ec8bd4f0-5df1-38fd-a480-142e1a5ae93e | -13.2414 | -46.8473 | 2025-08-05 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c34a865e-4020-3c45-8956-a08adc30a916 | -12.71366 | -48.10407 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab59df9f-ceab-32ed-8e63-c05b8964a2fe | -14.05258 | -41.99161 | 2025-08-05 04:19:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 65e185a3-0af0-3656-8701-b1dff6d819be | -12.71443 | -47.79322 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 661af43a-5b82-3aa3-b304-851466713acb | -12.70272 | -48.07914 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3dea72d4-3190-34ac-bf4e-9b03f677f49a | -13.05223 | -56.87308 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d58b4d4a-c556-3ac1-9652-7adaaeadfbea | -13.05751 | -56.8798 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6b4722e1-a3ad-3f8f-a122-3fbed3cbad67 | -12.99248 | -47.46086 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6520f688-fcf3-3ba2-8617-6ac793f2699d | -14.37672 | -50.32827 | 2025-08-05 04:19:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b9f8f51-a84c-3c81-99d4-ccaaeeded58e | -21.31536 | -43.75867 | 2025-08-05 04:19:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 71cfafdd-4c60-3041-ac07-d7fb8f826ec6 | -12.99319 | -47.45671 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfc04fba-c1a7-35a7-bea9-bdfea34274ee | -13.07142 | -56.88467 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 597c20db-bfcf-3a8b-b61d-9b090676af90 | -13.05861 | -56.87446 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e77300c3-d5b8-3b7a-bea3-13f7a6c8c0ab | -13.08716 | -56.90503 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 9e12a0d5-78ad-3290-81e7-d316a5366b85 | -13.07252 | -56.87948 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2c026139-c247-35e9-98fd-90f5ff73169a | -13.4264 | -47.46177 | 2025-08-05 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a2b79ca-8eb7-311d-a604-7c6c683c7a35 | -20.06505 | -43.70833 | 2025-08-05 04:19:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 74cedd87-1910-334b-a9a4-df8934a900af | -12.98994 | -47.46634 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dbf219d0-1747-380b-a2e0-54b095219d0e | -12.43544 | -48.71089 | 2025-08-05 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c69730eb-eb29-33c4-b981-6a326fc523f7 | -12.70571 | -48.08388 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf759fac-1b25-342f-81b9-17e01a1f04d9 | -13.04541 | -56.9129 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57c3074e-80af-31ad-9582-cab6eb649afc | -13.42995 | -47.46235 | 2025-08-05 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 14308c60-7766-3db6-8c11-36523164a341 | -12.71312 | -48.08509 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d1abea8-ef94-3850-ae95-89444e10e31f | -13.05231 | -56.88041 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| aa3a3b58-45a9-3f0d-8468-7d5c43651d4a | -13.06389 | -56.88122 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d8eeca3b-e105-3f71-b93b-640cf505cf77 | -12.44229 | -48.71714 | 2025-08-05 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a40feda-fcb9-3f6b-931d-7cc5222a7dd0 | -13.05983 | -56.87642 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 991b754d-f0cb-3325-bbbb-4604c586427a | -12.67945 | -48.12548 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca4d1afc-f1c1-325f-a9ee-afba2f2168ca | -12.71682 | -48.08569 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75b9eb05-c895-3b5c-badb-a2e4e1d2a28a | -13.07858 | -56.91408 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| de3d4862-580d-35c5-9631-376e9b2c3091 | -13.07656 | -56.88443 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8eaeb6ee-9684-3bef-b264-060a9b46e0fd | -12.72621 | -46.3946 | 2025-08-05 04:19:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 655506ca-fa11-3eff-aa1d-eaa927fffaf5 | -13.0713 | -56.87756 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8b53b2ce-e775-3559-ba5b-e50c4b83e115 | -14.35075 | -47.09786 | 2025-08-05 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5289d845-6bc4-37a8-b8a1-39e397fc4d9c | -12.98706 | -47.46155 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6068d931-7c1e-311d-a85e-61cca41095af | -12.71895 | -48.09546 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b740f257-20a4-3bf1-ae2f-f25ffab5b13a | -12.69161 | -48.07735 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5611631c-3c29-3c62-b60a-c6d65f9803b6 | -13.0797 | -56.90874 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| aba6f03e-16c8-3143-8e4f-7a3bbb23b4ad | -13.0726 | -56.893 | 2025-08-05 04:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 109382bb-87d6-3ea7-ac55-2d3b82e9dcec | -8.9478 | -46.7354 | 2025-08-05 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| c51bf8a2-0f97-379f-be60-46a55b57746b | -13.0538 | -56.8746 | 2025-08-05 04:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| b8fcb492-bfcb-323f-94e9-9b3a21cf2ad7 | -13.0916 | -56.8913 | 2025-08-05 04:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 5795bb4d-d825-3373-bf42-cc97f95fe297 | -14.2748 | -51.9874 | 2025-08-05 04:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 6d509deb-009a-3c8f-bb0e-c54dfc82487f | -13.0914 | -56.9114 | 2025-08-05 04:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| fb335215-bdd6-37fc-a94d-2432b1cd21c7 | -13.0723 | -56.9131 | 2025-08-05 04:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| f7d7e165-f892-34f3-acd3-9061e87260ce | -8.9478 | -46.7354 | 2025-08-05 04:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| b6a15e58-bad5-3baa-b605-20f4c66ab289 | -13.0538 | -56.8746 | 2025-08-05 04:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| f8ba0813-d7f8-33f3-80a0-be8ecdb2014a | -8.01 | -43.13569 | 2025-08-05 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5722621c-629a-398c-86e0-59285bfd8978 | -8.21709 | -45.05834 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1af9efd-e3cd-33b1-99ba-6dd8527acf59 | -8.35927 | -46.56035 | 2025-08-05 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a55546b9-c517-3842-b93c-16d60c2fea52 | -7.56356 | -44.88394 | 2025-08-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04f93e6f-a0dc-3d4f-9667-5c69b3e884fc | -7.39142 | -44.64159 | 2025-08-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 31a0b04e-6edf-395a-a7bd-6e8200b89a2c | -6.68091 | -49.78961 | 2025-08-05 04:38:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9947c8fe-5f56-3144-b1f1-331078a84979 | -3.56923 | -49.50583 | 2025-08-05 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5177225c-a440-3ef5-91cd-df01b40fd784 | -8.85354 | -47.60759 | 2025-08-05 04:38:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e42da08c-f48b-37ef-bc79-749c129d34c9 | -8.24106 | -45.06189 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d5e2622-c99b-39a3-b77b-dcd5d535f33f | -6.96261 | -42.8665 | 2025-08-05 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.8 |
| 05aea31b-e082-3882-8d92-0f8d1c1b6d5b | -8.94534 | -46.73878 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 84eff544-c3ba-30a4-8690-f1798efe0bba | -8.26154 | -45.06141 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d16c9665-8c5b-3620-9fe9-63a78e5b132c | -6.67982 | -49.79653 | 2025-08-05 04:38:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69770f75-a372-383d-a01f-aee44c3fb0b6 | -8.27353 | -45.06319 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66714e2e-6dd5-3dac-84c2-60bd16100842 | -5.87321 | -50.14759 | 2025-08-05 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1c945a7-4116-3d3f-87d9-d49acc5dd4b0 | -5.78636 | -43.60637 | 2025-08-05 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ceff9baa-bebf-39a1-87eb-54b620f63ac6 | -9.05457 | -45.06085 | 2025-08-05 04:38:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README21.md)

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

## Dados Diários - Página 180

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c72863cc-5c35-3aa4-962c-4a294d8ace5c | -11.73068 | -43.65789 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 3f92ac8a-e643-31be-a35b-51f6eea33ba2 | -12.22874 | -44.7354 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 2809de1b-5f50-3714-972f-99194d1c4dbb | -11.8372 | -47.36697 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 42a54946-1665-34b0-8ae7-bbeae2fef339 | -18.09773 | -42.57271 | 2026-10-07 16:35:00 | NPP-375 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e0f74ee4-71aa-31e3-87f0-a4559b23711a | -11.74373 | -44.94096 | 2026-10-07 16:35:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1752a804-266b-37b0-badf-0eab3973ebd2 | -12.16865 | -44.74841 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| a7416590-d572-3921-9c58-a7f26d4a7f9a | -14.34374 | -48.80483 | 2026-10-07 16:35:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2b745c52-e050-3f44-b297-74e5ab98a6e8 | -11.85329 | -43.55807 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 51.2 |
| bbd655e0-e47c-3ac5-b237-1ba350916617 | -11.7735 | -46.78208 | 2026-10-07 16:35:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 27.7 |
| aebe67fb-28e4-30f6-8ea9-3d611b2c57ef | -13.10405 | -39.08818 | 2026-10-07 16:35:00 | NPP-375 | ARATUÍPE | BAHIA | Brasil | 2902302 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 1dd2a1c8-c0d5-31b5-9171-63019d38b7b7 | -11.62475 | -43.6713 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 02950d63-b1bf-3adc-aa5d-cbc0569bf240 | -17.49802 | -39.88577 | 2026-10-07 16:35:00 | NPP-375 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 29.4 |
| 8ec1bc40-230e-3350-b54d-156ca3660c5d | -11.23436 | -44.01834 | 2026-10-07 16:35:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 7b4dd3a3-4318-3373-8c25-5bf69c7b07a9 | -11.83661 | -43.56074 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| c906f4d8-0bbd-3251-addd-0e33a83838d4 | -12.66515 | -38.55128 | 2026-10-07 16:35:00 | NPP-375 | SÃO FRANCISCO DO CONDE | BAHIA | Brasil | 2929206 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f68d8322-aaa8-3867-a689-2715465709d4 | -12.17254 | -44.77507 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 122.5 |
| c2ff6296-fa4b-35d7-bc7b-8b61598b1ae9 | -11.83838 | -47.34823 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 60da625c-2838-3bd8-be9d-ea70efc39535 | -14.50764 | -41.44332 | 2026-10-07 16:35:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 65dc6706-bbe4-33d2-bc02-56cedfc937f4 | -15.45426 | -47.90856 | 2026-10-07 16:35:00 | NPP-375 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3670c94f-ab16-3763-93bb-e29f487dfd09 | -12.22475 | -44.73212 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 3776bdfa-cb1c-3010-b793-a2cdb39699c2 | -12.16078 | -44.71854 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| ecffd1f3-8559-3bf9-bdf7-16d8102cdec2 | -12.22316 | -44.73638 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 35.3 |
| e61313e5-a266-3169-9c8b-1286b7f18bd7 | -13.69502 | -49.10795 | 2026-10-07 16:35:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 51f5a602-6bb7-3675-805d-0eb9fb34236f | -11.62338 | -43.61699 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 8cf596cc-79d0-3ebf-a9af-c8f839a9ac34 | -14.35191 | -41.27296 | 2026-10-07 16:35:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 32.5 |
| d622fa8e-503d-30cf-96a5-325b100c942d | -12.8315 | -45.55793 | 2026-10-07 16:35:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 72df990a-43e2-3d03-9548-4a7db558c52b | -12.32312 | -47.94679 | 2026-10-07 16:35:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 462a9946-97bc-3b1d-9e04-3855e8a1a9ee | -12.22216 | -44.68976 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9233845a-2107-3879-830b-6c7ae2986ae0 | -11.63369 | -43.60374 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 153a4395-250e-3354-b531-a99177fafdf3 | -15.16351 | -47.91778 | 2026-10-07 16:35:00 | NPP-375 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e24c9fdf-d8fc-37c3-9cd3-c8ab744a3160 | -11.23268 | -44.8738 | 2026-10-07 16:35:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 824fab58-3939-3903-8cdb-128a9d7fe32f | -13.6025 | -41.06165 | 2026-10-07 16:35:00 | NPP-375 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 24.0 |
| 70c68bc0-067b-3b16-89f0-8557fe6bd578 | -11.61993 | -43.63935 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 845700c3-2e85-33b7-87a1-417985dbf762 | -19.01636 | -39.87716 | 2026-10-07 16:35:00 | NPP-375 | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| daa1a2a5-4c74-31fa-9d7c-be25b9a1acc7 | -13.33377 | -39.00886 | 2026-10-07 16:35:00 | NPP-375 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 78c079db-038c-3cef-9aab-00dc1a4a297c | -13.37572 | -40.86446 | 2026-10-07 16:35:00 | NPP-375 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 7cba307a-4de0-3455-9836-1afe8ed980c3 | -11.23427 | -45.24799 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 503ddb00-706a-30e4-a87c-08f7370e4fcb | -12.17543 | -44.77073 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 24c48bed-a19b-3be2-b141-a8aaf07dd7b9 | -18.55235 | -40.64879 | 2026-10-07 16:35:00 | NPP-375 | VILA PAVÃO | ESPÍRITO SANTO | Brasil | 3205150 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 55cc6156-e188-3e16-afb3-f6941a4ba152 | -16.85515 | -40.58548 | 2026-10-07 16:35:00 | NPP-375 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 540e4f76-61ed-3865-84c0-1ca07cabc029 | -10.94487 | -39.48442 | 2026-10-07 16:35:00 | NPP-375 | NORDESTINA | BAHIA | Brasil | 2922656 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| f79e3480-c71e-34fb-8e87-c72427d80a2e | -11.83768 | -43.56789 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| bbc63d39-afef-37b0-8b1a-78975eca89dc | -12.1892 | -44.76865 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 223387f7-bc40-3f96-afbf-98e2126e556e | -14.28752 | -43.19176 | 2026-10-07 16:35:00 | NPP-375 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 6d7014c6-6dd7-3401-9882-c9a3e59feecf | -18.34171 | -42.3889 | 2026-10-07 16:35:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 6e7af972-6ba6-384d-b173-257bbadcbfca | -18.34114 | -42.38514 | 2026-10-07 16:35:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| ece3b1f9-aa08-3a48-9af4-aef7fa7cac78 | -12.82493 | -45.56312 | 2026-10-07 16:35:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 352af50c-94e7-35d0-b7ed-407ed7046bd7 | -11.23774 | -45.24746 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 5bb409c4-ad38-37e9-8867-356b649024f6 | -14.04367 | -40.45472 | 2026-10-07 16:35:00 | NPP-375 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| d386f147-e9ba-309a-b40b-d4311c935cc7 | -11.71451 | -43.66403 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 110881ff-15fe-35dc-9c2a-b34dbf92632b | -14.21505 | -41.37337 | 2026-10-07 16:35:00 | NPP-375 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 7bce2320-9262-38ff-846b-148629f887a1 | -14.67811 | -53.08624 | 2026-10-07 16:35:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db159724-1328-3b2c-aa1f-e83df92b5332 | -18.55556 | -42.6565 | 2026-10-07 16:35:00 | NPP-375 | CANTAGALO | MINAS GERAIS | Brasil | 3112059 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 0ea2e4aa-16b3-37fe-8c3b-5ba6777cf5c9 | -12.2085 | -44.66104 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ad50860e-d0e3-375f-b8ea-b989c956dd4e | -10.53257 | -40.23129 | 2026-10-07 16:35:00 | NPP-375 | SENHOR DO BONFIM | BAHIA | Brasil | 2930105 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 84d8647d-ea75-315d-a58d-b7442f6bd204 | -10.85093 | -42.80676 | 2026-10-07 16:35:00 | NPP-375 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| bd8021ac-6062-3f90-990f-95bdfbd99d11 | -11.77773 | -46.70143 | 2026-10-07 16:35:00 | NPP-375 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 41dc9068-3c99-3940-9ca8-40f264903916 | -18.18521 | -42.34146 | 2026-10-07 16:35:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 747627eb-1a3d-3167-80de-2384430a5a7b | -18.47134 | -40.86541 | 2026-10-07 16:35:00 | NPP-375 | BARRA DE SÃO FRANCISCO | ESPÍRITO SANTO | Brasil | 3200904 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 1785889d-47b7-3f60-8646-3443826cda9f | -11.84119 | -47.36816 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 074cfa8b-2de9-35d4-b8e2-8c9227d72264 | -17.49401 | -39.88256 | 2026-10-07 16:35:00 | NPP-375 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 29.4 |
| b1e046b1-b026-35bb-a600-64829e080b9a | -15.11208 | -48.50687 | 2026-10-07 16:35:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4a09e536-e848-3998-bcde-f3e946d21a40 | -13.69329 | -49.09409 | 2026-10-07 16:35:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 31.3 |
| b4227c84-e9d5-3af4-9b1e-ed308aa861a8 | -16.89748 | -40.87579 | 2026-10-07 16:35:00 | NPP-375 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 61347242-633d-3ae9-9803-200024b0a49f | -12.8291 | -45.56675 | 2026-10-07 16:35:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 101cb1a5-77ac-320b-a782-691f06df8af3 | -11.62581 | -43.67834 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 04d174b4-48d2-3da8-a000-625b60fb6fb4 | -13.39137 | -43.87474 | 2026-10-07 16:35:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| d3b732ec-96a1-33a7-a3bc-c57c265c3997 | -10.45491 | -40.02624 | 2026-10-07 16:35:00 | NPP-375 | SENHOR DO BONFIM | BAHIA | Brasil | 2930105 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 34b52992-50ac-3e81-aa08-f7b822e43efa | -12.26889 | -47.17413 | 2026-10-07 16:35:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| a421265f-6e8f-38e2-b058-b9b7ac97282c | -12.31185 | -40.29544 | 2026-10-07 16:35:00 | NPP-375 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 31bbc103-8e87-31bc-86ad-c5fa2462a01a | -12.32362 | -47.95045 | 2026-10-07 16:35:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 95bcbdec-f0d2-3038-b243-e7578bbcd84b | -17.43516 | -43.64413 | 2026-10-07 16:35:00 | NPP-375 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 50b8052b-9105-3758-af61-12ae08af93ed | -11.64541 | -43.68189 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 85aaa45b-d468-34c6-aae7-9a411fd73eef | -13.37392 | -43.87368 | 2026-10-07 16:35:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 97f9754c-adf1-3b5a-82df-d6bb3985d768 | -11.26061 | -45.18484 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0f06089d-14fd-369a-bf38-93eb01870861 | -14.0833 | -43.77035 | 2026-10-07 16:35:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 99cba7f6-a5b7-3e1e-8be3-5a7b2e0c513a | -16.85574 | -40.58916 | 2026-10-07 16:35:00 | NPP-375 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 57d5c2d7-fa76-3dbf-9af0-37c6bca41216 | -14.86859 | -48.44481 | 2026-10-07 16:35:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2162e281-7bf1-3698-ac6c-bb7a78a0b3ce | -13.50277 | -39.96365 | 2026-10-07 16:35:00 | NPP-375 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| ea56f3b0-82ff-3bdd-8d65-a3fc442ee377 | -12.20339 | -44.65021 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 22377f04-7be7-322b-b7a1-8670cf0d263f | -11.22966 | -45.29609 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| b99f05d5-e13f-32fe-8b3d-c1bbd6f02c52 | -12.18455 | -44.78494 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 71b57be7-2698-374c-8378-3fd9578ab868 | -13.67831 | -48.79562 | 2026-10-07 16:35:00 | NPP-375 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 7a1cc542-73a4-3f7b-9e90-ad87fcc2638b | -12.18054 | -44.78165 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 312.2 |
| b60b0ffe-0022-372a-b211-bf20b9c6c16b | -14.74456 | -49.52037 | 2026-10-07 16:35:00 | NPP-375 | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3492a6bc-c47a-3b3f-adef-76d25bc0d2e0 | -11.22814 | -44.86679 | 2026-10-07 16:35:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1138c239-5683-3dcb-9cb6-4193a55195eb | -10.55022 | -40.29541 | 2026-10-07 16:35:00 | NPP-375 | ANTÔNIO GONÇALVES | BAHIA | Brasil | 2901809 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| a9f5b869-0a5b-35b2-af86-4bd03c1e4fdb | -14.59 | -42.41873 | 2026-10-07 16:35:00 | NPP-375 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| ed5f7f15-8d46-322d-b841-6fccfa0b003b | -17.74919 | -45.40086 | 2026-10-07 16:35:00 | NPP-375 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 581552d1-43a6-346c-96ea-1d5b93c09936 | -11.84332 | -47.38322 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| ec53b431-a261-32f3-9a43-6453668cf1a3 | -11.76933 | -47.73554 | 2026-10-07 16:35:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 20960283-c104-33c6-bc16-0331e0eee004 | -12.21979 | -44.71358 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| a4d8a832-423e-3386-9fc6-d6c02c875439 | -11.74984 | -38.44397 | 2026-10-07 16:35:00 | NPP-375 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 2c3a3813-1dd4-3569-911b-9b8f38948746 | -13.80826 | -52.79775 | 2026-10-07 16:35:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 369e6f8f-5e09-3420-b711-24d0fab4962b | -12.2266 | -44.73586 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 35.3 |
| e7d10a55-3b97-32b2-bab6-4a1ab700d236 | -12.17887 | -44.7702 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| e4c94e1d-8163-38cb-a1b5-15398b117a8a | -13.49603 | -46.65435 | 2026-10-07 16:35:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 9c96f4c4-17f9-364c-97e6-fc7fe7ea51cd | -12.17099 | -44.7403 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 171.0 |
| ebf5a2cb-1bcb-3846-86ef-d9c3dfb26d90 | -13.80902 | -52.79776 | 2026-10-07 16:35:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fd0cf5a3-a885-3d0b-a3e7-aef679585ff5 | -11.23079 | -45.24852 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |


[Clique aqui para ver as próximas entradas](README181.md)

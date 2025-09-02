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
| a46cb489-0337-3271-915f-b32cc7bf67aa | -11.8087 | -46.40192 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58bae94f-fe7b-3e66-a2e3-c07a03904391 | -8.81678 | -47.4858 | 2025-09-02 04:14:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4b257770-1127-37cb-9e89-e9c302edcaad | -11.10539 | -44.62827 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| b7897b79-e76c-3e71-ba17-0a5ef1b13062 | -9.73478 | -48.96426 | 2025-09-02 04:14:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee412580-8eb4-3d23-97c1-67f3bde4b911 | -12.76209 | -48.09021 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0e396786-f5c8-38f7-9ccb-79f9925e347e | -11.85844 | -46.7181 | 2025-09-02 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf965784-cc45-3059-9f79-ffe97b688784 | -12.88728 | -48.17011 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d760f7a-5add-3585-b406-41fa6634da9d | -8.13035 | -45.02979 | 2025-09-02 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 299410e2-9973-3cd0-a77d-5d8ee86dea1f | -7.12222 | -44.56871 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e4c8ae11-f896-326f-b470-557cc186d49c | -7.6753 | -43.87469 | 2025-09-02 04:14:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 44c5953a-d7c8-3e6e-a94a-03844036b296 | -10.97059 | -50.78267 | 2025-09-02 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4a3e2e4-39ad-312f-af61-ce849c59390a | -11.06492 | -46.91434 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c97964e-7b09-3f45-87a1-a6db3fd6d31d | -7.92408 | -46.44031 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72952ce6-cf50-336b-b1ed-e006ac697cc6 | -12.95344 | -48.09095 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2f2d68c7-525f-3bfb-a521-72e5ecb4dacf | -13.68791 | -46.92299 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bc19db9-756b-3c16-a297-ef58aaa4f141 | -11.04364 | -45.14405 | 2025-09-02 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7b8c1469-eb63-38ab-b5bc-21c032dce6f2 | -10.3978 | -47.12539 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b72ee21-1471-38e9-ad43-34c5b5335e6a | -12.98652 | -48.09481 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 69d6f17d-a88c-309d-94aa-622ce5f91ee4 | -7.7898 | -45.44733 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 596cf7e2-887b-3d7c-b265-d0ea3ea1b6f1 | -11.65568 | -44.86268 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d32ec301-304a-3f77-a807-a626de26e258 | -11.64975 | -52.17034 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 46f8f216-82c0-3847-bfcc-992e8ef65554 | -14.05201 | -44.54834 | 2025-09-02 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35434730-e550-35c4-b82b-627f963f3c69 | -7.48401 | -45.36444 | 2025-09-02 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 790ee5d5-191e-3456-813b-9cc0f0b69c8a | -11.37868 | -43.60344 | 2025-09-02 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8ce3421-e758-387a-8754-4c77db7e8e50 | -12.46746 | -43.20502 | 2025-09-02 04:14:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1eb56a5b-fd0c-3c6a-bbc9-7391eff8a166 | -11.02572 | -47.12923 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| de7e6094-8e2e-3c97-aad9-79dfffdb005e | -11.66805 | -52.17917 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 9689432d-f509-38a7-9981-f9b55d0bcd88 | -12.62912 | -48.16356 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10c3bd48-32e3-3c63-a6ac-d09d2e9066c5 | -7.55989 | -45.69889 | 2025-09-02 04:14:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78ad1cd6-e012-3f7b-831b-7405c8155fb7 | -10.45823 | -49.05989 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 92c9aec4-5165-39eb-a59c-7593baa7a27f | -7.55927 | -45.70273 | 2025-09-02 04:14:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b531a197-2e4e-3ff1-a255-5e063390fdb0 | -12.64764 | -48.25419 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e2a29455-101e-322a-93a5-4fe8e139370a | -6.83135 | -52.82954 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9453a47-e8a4-3437-8388-0a3f60464024 | -12.62239 | -48.18046 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| b63f16af-dd6b-3b48-ae5f-efefc6dc69e9 | -7.98002 | -46.47935 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 595f9c98-e50b-3271-a0cd-f2c36cbabea1 | -12.57718 | -44.79268 | 2025-09-02 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fbee4dd-f7ca-3771-967f-fa0dc423e294 | -11.10096 | -44.63477 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8e264b07-26c4-305d-8671-f7fed74cde16 | -11.0535 | -46.89575 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1dce0185-a737-33dd-ad34-a4901a4cb79a | -10.03578 | -48.05632 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec84a2bd-526e-3b06-a777-59813095c8b4 | -9.44243 | -48.86539 | 2025-09-02 04:14:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cad8deb1-0d13-3678-bbac-4a5527f760b4 | -6.78876 | -52.81238 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0fbd9665-877d-36e5-af4b-ba520ec3d230 | -11.42564 | -55.19188 | 2025-09-02 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7d030ed-86ad-3d1a-ae42-d712ec786bbc | -13.47005 | -46.92477 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72978adc-0e9d-3677-b525-b81b15a6a384 | -6.80061 | -52.81247 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c5b973d-ed13-30fc-90c1-2f53242e086f | -12.61437 | -48.24842 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a267546b-c59a-3b93-a960-132f3a0e1154 | -13.28556 | -46.91045 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27feaceb-1208-31f9-857f-b9b12578aee1 | -9.2237 | -47.07898 | 2025-09-02 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06cd3c6d-532b-3110-abd7-556e3003e6cf | -10.439 | -54.77529 | 2025-09-02 04:14:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2866c701-5db8-3100-b556-55345ac4d880 | -10.73176 | -44.79896 | 2025-09-02 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2b11008-3598-3242-9f4f-0bfd39d7f287 | -11.06206 | -46.90968 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f17e56a-6466-33c7-a109-49dbfd1ec1a1 | -9.23597 | -47.05048 | 2025-09-02 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e098cf25-c505-33d9-b0a0-895c3add4ded | -7.0653 | -44.58977 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0970734e-7bea-39e5-aba9-4c232859922e | -7.70454 | -44.60722 | 2025-09-02 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6bdf0e3d-a2f2-35a0-90b9-556625c3ea05 | -11.67175 | -52.21354 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 7f57901c-c7f6-31b2-959e-cf7a4cdc051c | -11.09486 | -44.65181 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3827cceb-465b-3a4b-aca0-55c7e0590825 | -7.70789 | -44.60776 | 2025-09-02 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfc40f18-99cc-3619-a45c-8f85f495af3a | -6.79481 | -52.81002 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5e947d81-ef8b-3771-9c20-80f8d94c703b | -11.00591 | -46.83405 | 2025-09-02 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 28e355f6-5d09-353c-9dee-11fd67c992df | -11.1048 | -44.65343 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c47ffb08-4ed0-3a3f-8e3d-18093224af33 | -8.05048 | -52.35509 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc2f8d76-bd93-3038-95c4-82c391c5994c | -7.48773 | -47.88365 | 2025-09-02 04:14:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8895115b-5068-3563-aabc-ff1b6da38da2 | -8.25973 | -45.61845 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 11bbd074-a46f-3a88-ae02-725ca62970ca | -13.69896 | -46.8772 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 28ab9145-9d3f-3703-8c32-cac5c45b3e58 | -13.30551 | -46.83359 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 43272548-9ead-3e5e-9d61-bc3bdc8b2e3e | -12.99069 | -48.11429 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a61be864-6023-3f75-b021-ca723c195afc | -7.26464 | -46.15651 | 2025-09-02 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b04f680c-2e3e-3f46-a890-8ccdbb1c63d3 | -12.96387 | -48.09538 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ae29487-df84-34d2-8ba3-f0bbba8df7bd | -7.19754 | -43.26526 | 2025-09-02 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a0badab1-5f3d-39fd-90d9-30d71e3048e8 | -7.99207 | -46.47294 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1cb83c36-6e46-3e50-be34-d83f7fa2eec9 | -7.91849 | -46.45187 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a86f8600-1b28-3754-b763-6e24d2027675 | -11.86127 | -46.72262 | 2025-09-02 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09c91ee4-c0f3-3d11-9c71-70224363ce44 | -12.37857 | -46.47684 | 2025-09-02 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c7051d0-a770-3b75-ad10-5d7c41788c45 | -6.81059 | -52.81644 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 29e353b5-df31-3cd5-8a38-ca2b1334654d | -6.81897 | -52.83304 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 118a3fbc-51cb-3702-aa15-6808145a319a | -13.3096 | -46.83025 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6589ba7c-d455-32c0-8070-fba8b5920c52 | -7.54797 | -45.72848 | 2025-09-02 04:14:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c04f6b8a-f396-3c32-b86d-93d3195c0d62 | -6.8221 | -52.81505 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28cb7e5e-6b86-3b59-aa2c-ab1345f95e51 | -13.69353 | -46.93188 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b7cf7fdf-d436-334a-8941-16555fffe811 | -10.25812 | -47.52738 | 2025-09-02 04:14:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 327598ca-4d93-3d87-a984-abfa0811af82 | -12.56837 | -44.78401 | 2025-09-02 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b42bb308-0088-3999-8903-9f8211905244 | -8.45965 | -43.61853 | 2025-09-02 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d7b452c7-f7a1-3867-8b81-992d3ccf3d6a | -11.88622 | -46.67907 | 2025-09-02 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 552ad184-a845-38a7-99a1-859dffda7485 | -12.5646 | -48.25998 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55d27805-913b-3c5b-b9a8-7562c956d3bc | -8.46208 | -47.37374 | 2025-09-02 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0bf98ad4-266d-38a2-9ee7-f6718ef21e85 | -13.28192 | -46.88984 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 72860664-20a0-3ecd-835e-36fc18a01065 | -12.85872 | -48.05172 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fd63cd88-ea61-3065-941a-895425bdf766 | -7.11277 | -44.75527 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9625e125-4054-3b59-aa61-142a423312da | -13.53972 | -46.98953 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e5b2c4fa-21c1-3a97-b64d-3ae139726d41 | -6.82524 | -52.8321 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9f07b282-cb9a-3503-b853-a456e56f16b0 | -10.83371 | -47.45002 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ea845d6-6a82-3d8c-9992-91cb2966d218 | -11.0066 | -46.82996 | 2025-09-02 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9c2b68cc-5aba-346e-8a39-f66133b44db5 | -13.32742 | -46.95763 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93bebfcd-4498-38d1-8a7e-27fdbcf0543d | -11.90688 | -46.67433 | 2025-09-02 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ba9f4c6-c158-32a8-89a7-27ac6b174f3a | -11.65244 | -52.20992 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e30b6045-2306-3235-9723-7b57f10c4c8e | -12.78038 | -48.09337 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6c238a7-fab3-3d5a-87ef-5e32194c8916 | -7.9278 | -46.4621 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4b4db34-b1f8-3504-ac53-9a01d2af66c3 | -9.64915 | -48.568 | 2025-09-02 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11ef76a0-176f-3ac3-ac08-0fa00098ac31 | -7.66072 | -42.71485 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4ff374c1-1216-34d6-ab58-9508ea6a5940 | -11.89688 | -44.88432 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cd4d64b-f1c9-3afb-a4cc-1329f75089ec | -7.63722 | -42.65015 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README44.md)

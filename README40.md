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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 632bb768-88ec-38c2-a9e9-fd04bcf7cae5 | -13.51501 | -46.87563 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5025e8c1-662d-390e-bfc9-7a84eb52719e | -13.62694 | -48.2429 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 504238e2-0ca4-33f3-85ae-5fdacf630280 | -8.26752 | -45.17136 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2e3d3018-3f24-3690-9eaf-1e5ab3bfc250 | -11.03563 | -45.14083 | 2025-08-28 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98209545-3deb-3222-9e3e-0351aa7909c5 | -11.32348 | -43.5421 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a87147c9-eaa6-3537-9e9c-7a795fd4e2ac | -8.29329 | -45.15013 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 844852c6-43d4-347a-83ee-ed4b3aef38a0 | -11.32015 | -43.54155 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8999a8a9-8d73-3523-9751-d81363bcf59e | -7.77049 | -45.47345 | 2025-08-28 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 16c572bc-cd2f-37ac-859c-887fa5a2d6ed | -8.46838 | -43.65411 | 2025-08-28 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 38e9556d-93c6-3b83-ba92-27ca282192e9 | -11.92315 | -46.7045 | 2025-08-28 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28e9f43b-a011-3748-be43-aa051e5266e0 | -12.86305 | -48.11651 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ffa2e580-cfff-3d23-ab00-ca669fe6e2d8 | -6.49395 | -53.39765 | 2025-08-28 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75178141-a2a0-3668-a663-d7bc55fdae01 | -12.68705 | -45.08513 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9a6a4b49-0da3-3a20-8b0d-e8a3cf046a1e | -9.65051 | -40.59942 | 2025-08-28 04:08:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |
| e92637be-3f28-37da-aab5-92b0f28988da | -13.41887 | -46.99926 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dce3ae0b-5689-3d64-947f-e98625ff4e1b | -12.89219 | -48.11531 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 55dd239b-fc43-3041-8560-6e0043910df3 | -11.33623 | -43.54785 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e630a869-9dae-362e-9644-1c64546a397e | -13.18313 | -45.28962 | 2025-08-28 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2e5f2c93-bf51-3172-93dd-bcac20b532e6 | -11.27944 | -43.30578 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ae7a0b8-1569-32c1-88e0-59612ecf68db | -13.53964 | -46.93099 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 301951d5-f758-356a-aedd-cee132aa7de6 | -10.09807 | -42.42369 | 2025-08-28 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 089ac481-6280-3d49-ab0f-68712c9130b0 | -12.78069 | -48.1765 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e60baa2e-a4a8-3cf4-bd56-6a4771096b3c | -13.21348 | -43.14808 | 2025-08-28 04:08:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4335da24-cc0b-3779-af4c-ac03ad704874 | -9.4494 | -51.96431 | 2025-08-28 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 661bf37e-0779-39d2-b9e4-e5f295872cb0 | -13.086 | -46.33907 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 52070a97-f65c-3950-85d5-cdc57696fd07 | -13.17408 | -45.28013 | 2025-08-28 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c2f63856-59d1-3ef7-9aa9-4a4c227bed3e | -8.47633 | -43.64788 | 2025-08-28 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a398ffe-386f-34a7-8240-7d1840c856b7 | -11.3424 | -43.53064 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 58c956fc-29ca-3981-85b0-bd0d5fa6d234 | -12.67561 | -48.17963 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c2a6deb3-27d8-3577-a17c-aa4022cbac0d | -13.42296 | -46.97567 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97c9dad0-d108-34d8-a9ab-98678f9b9a64 | -8.28554 | -45.17442 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 794767cd-8e42-3cf7-9cd1-4418196c2dc7 | -9.04138 | -42.79084 | 2025-08-28 04:08:00 | NOAA-20 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9226db4a-d77e-3bfe-8186-6a5f1abed297 | -11.21413 | -43.37474 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4a8aaf37-d1fc-3d17-b028-838b3e26100e | -11.55073 | -46.36237 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 66e29409-5c0d-3d5b-9357-283817f1e412 | -10.52927 | -46.69859 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 12a9dbf5-f0e2-36d7-8d7f-4808d669c085 | -12.40826 | -46.48271 | 2025-08-28 04:08:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 32af8e47-de2b-3ad5-8c67-70a777a8a29c | -13.63562 | -48.24036 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a43a644c-0414-3e8b-8763-397618a90f09 | -13.42921 | -46.85181 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 66c644eb-dc2e-3293-bdd8-d322a6e51f3c | -11.34335 | -43.54158 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 21036dcf-6687-3f63-875d-3b15ee5e91d0 | -12.70651 | -48.16938 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3aef7bfd-75d1-3518-ab2e-fce9d52e45a9 | -12.78385 | -48.15876 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bab3a0d5-4804-3b26-89aa-b647692e27da | -13.08239 | -46.33849 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 684b15f1-e0c4-349a-814d-6c117856e4cd | -12.89477 | -48.1008 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 217ebb98-d64b-31bd-b3a8-7190cb78ceb4 | -8.24861 | -45.14393 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3d77c95a-04b2-3528-8f49-297dac8a198f | -12.67897 | -48.18414 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bd0a4f52-68c1-39ad-a2ad-31067fad4f8e | -12.44157 | -48.71138 | 2025-08-28 04:08:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f804d984-9a03-35ea-b1aa-5ec0162061e6 | -8.27416 | -45.19821 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d21b1c67-c54f-3e60-8ce8-39431099f257 | -10.53689 | -46.69983 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 758b27cf-f7e6-3d97-be3d-6b2d3c823a92 | -9.67354 | -48.31316 | 2025-08-28 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 810eb235-ee49-341d-96af-40caccfa6f6e | -8.25241 | -45.17305 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 55fb790d-c3a0-33bc-81fc-45e1df9ae174 | -12.89811 | -48.10523 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d6e665a-987a-3dbd-979f-862010ed3b36 | -8.44051 | -41.4526 | 2025-08-28 04:08:00 | NOAA-20 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 96.3 |
| b92bd384-8729-303e-9cc6-ff767782d4d5 | -8.28969 | -45.14952 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| e226a9d6-0a63-3275-9618-580b29706833 | -8.28263 | -45.16967 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1ef1e5d7-08a3-34d8-88c5-7267ef9c06db | -13.5456 | -46.91857 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e224dfd-ae23-353e-af4b-d4558defd5f9 | -13.97683 | -46.35151 | 2025-08-28 04:08:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6e2ea22-1d18-3105-a9c9-2297fe435c13 | -11.56906 | -46.38826 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 71380171-5160-3f11-8bbd-770e8fa5ff1c | -8.44833 | -43.69223 | 2025-08-28 04:08:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ee0c209-1ef4-358d-a996-1cb4b115269e | -13.52158 | -46.88154 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dc910d17-b75d-3e73-aaf1-3bbb40c19366 | -8.49421 | -44.74705 | 2025-08-28 04:08:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d60c1cc7-5efe-3221-aece-df94f0d74db3 | -11.56023 | -46.39547 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2afb0221-ca23-3898-a7f6-ec5061fec33f | -13.51827 | -46.92235 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8eeb9b42-efd6-3235-ada9-92cf01d80176 | -7.8946 | -44.77675 | 2025-08-28 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3996b726-0c6f-38c5-83b5-68a39da10862 | -11.22591 | -55.0524 | 2025-08-28 04:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f8d72341-fcba-34b4-9ad7-820df4afde2e | -13.0789 | -46.31554 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 03905c62-ee5b-3a81-897c-e9eb9707b0dd | -7.89106 | -44.77607 | 2025-08-28 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1170d4f9-43eb-3f59-ba7c-19ce39e8edb1 | -13.82933 | -46.68787 | 2025-08-28 04:08:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa6161c8-52aa-321f-819a-527d28813223 | -13.41941 | -47.01824 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 704f5b19-cf87-37b0-b5e6-d7caf916b5fe | -13.51754 | -46.92654 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c66e8062-8273-3e5a-9933-d58f989d8c2d | -13.38739 | -46.88305 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7da8156f-3092-3325-bd44-c47ed84b3617 | -12.79252 | -48.15665 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5cfa26df-66bc-3e8a-afcf-bd3d29f860fb | -13.4418 | -46.84494 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d13dac21-2ce2-304a-8026-50305de47b52 | -13.66777 | -46.88478 | 2025-08-28 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 102bee5f-6cac-31ee-b61f-dc5f3012e083 | -9.67959 | -47.07066 | 2025-08-28 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 42cd1233-6a74-325c-bc12-01fca41b34e0 | -13.42044 | -46.99019 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f865e9c-d68a-32b6-8010-35b55452882b | -7.76589 | -51.06347 | 2025-08-28 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 106deaf0-6732-3a84-8b8b-c4771551bca3 | -11.57113 | -46.42067 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ae091dd4-d08e-36f7-a213-f261636ab4f8 | -13.45214 | -46.85105 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c6001de3-319c-311c-a296-5e2073a160d9 | -12.80398 | -48.16215 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a7af859b-cc56-3dc1-822c-2fd2305ba173 | -10.53931 | -46.6857 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba71fa10-790c-35d3-9017-c7dc66862578 | -8.90308 | -47.32803 | 2025-08-28 04:08:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e39946e6-d9c7-3f7d-ac91-92981432737c | -7.23433 | -45.42904 | 2025-08-28 04:08:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0b40e702-b755-370d-9955-a4b85e1f31cf | -11.32795 | -43.53555 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c4144cd-608f-3905-9c2c-7ec87552f2ea | -13.52196 | -46.92305 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 67619286-32d3-3efd-a56c-1ffc731e094b | -8.28109 | -45.15665 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8571b10b-e2da-3466-b29c-e73dcfee491e | -9.44872 | -51.96656 | 2025-08-28 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| adcf246a-f962-378e-be1d-e7e9438844c5 | -8.28915 | -45.17502 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a97b9d91-b48a-39e8-96a4-9c7fcedd249a | -13.5064 | -46.85974 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fcb9cc7d-cf70-35e8-a899-b5603b6ddf03 | -8.28401 | -45.1614 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 8d55b0d5-f601-3138-8164-d6ee77c942fc | -9.05361 | -54.94469 | 2025-08-28 04:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 775f1068-e852-3cc1-b830-c22e444034c0 | -13.08331 | -46.31145 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c58567b8-3a28-3a95-ab8c-8dfb648432ba | -8.45672 | -43.70491 | 2025-08-28 04:08:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae974570-5c0e-3f96-b1ce-abcc7f0f2668 | -8.24149 | -45.07435 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9279e94f-530f-367e-8540-2eee8088b6ef | -13.38589 | -46.86949 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b691f4b0-69dd-3ce7-995e-cec65b12721f | -11.74731 | -49.08889 | 2025-08-28 04:08:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f99f09a2-54b0-3a65-bf80-f7e83bebb171 | -14.13469 | -45.41323 | 2025-08-28 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f24c7bdb-ab98-3158-bd6a-4660290d1595 | -8.29053 | -45.16673 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| efa8b036-d6d9-3850-a86f-f6df572929a9 | -8.44111 | -43.67226 | 2025-08-28 04:08:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 173f8638-8cfe-36dd-bea7-025ee11ffdcb | -12.81115 | -48.14503 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| acdb2b60-2584-338e-9271-b49d9f2aa577 | -12.67813 | -48.16543 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README41.md)

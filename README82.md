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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a65d30b4-cb4c-3649-83cf-aaeb11d1cc6e | -20.94174 | -45.79873 | 2025-09-10 04:46:00 | NPP-375D | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 08df80ee-8faa-38bc-af0e-93c7a34884c4 | -20.1027 | -47.82445 | 2025-09-10 04:46:00 | NPP-375D | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a832ae76-2a35-3323-a608-0375b6dbcc1c | -21.12474 | -47.73479 | 2025-09-10 04:46:00 | NPP-375D | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 000aa308-bf45-3db8-bb89-957d15088452 | -20.93267 | -45.79768 | 2025-09-10 04:46:00 | NPP-375D | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 528e303d-d807-3ca7-bbd8-35aec7161888 | -20.55028 | -47.61749 | 2025-09-10 04:46:00 | NPP-375D | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ece49833-b1b5-3fbb-906e-4c3d8b699e4b | -22.03373 | -42.90017 | 2025-09-10 04:46:00 | NPP-375D | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 53b1fc53-5094-388b-ac56-6f5a30d4043c | -20.07505 | -47.53654 | 2025-09-10 04:46:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 58445934-afd9-383a-b528-a0c3e63de185 | -20.53194 | -47.66491 | 2025-09-10 04:46:00 | NPP-375D | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75639ac9-b244-32b5-8474-47e06d1b94df | -21.02551 | -48.42395 | 2025-09-10 04:46:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb7401c9-bc29-3bbf-ac44-423c461a07cb | -23.70555 | -51.78658 | 2025-09-10 04:46:00 | NPP-375D | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| c1d5d5fc-33c3-38db-92ea-7ca677ac7157 | -20.46678 | -43.95245 | 2025-09-10 04:46:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| d7c90181-3d3b-3774-b7f0-da79492fd4fe | -20.52884 | -47.62547 | 2025-09-10 04:46:00 | NPP-375D | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1be6e513-8090-3bf2-b010-ca9c53011228 | -20.00763 | -47.63642 | 2025-09-10 04:46:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 308f50d8-9f16-3024-b8e8-f83a004caca9 | -21.77804 | -45.56905 | 2025-09-10 04:46:00 | NPP-375D | CORDISLÂNDIA | MINAS GERAIS | Brasil | 3119005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7f313d73-fa22-3f5c-8047-42bc6ce4ac92 | -21.18654 | -45.11713 | 2025-09-10 04:46:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 13c1a57d-0da4-3cf9-9d93-11de71f2da98 | -21.12074 | -47.73409 | 2025-09-10 04:46:00 | NPP-375D | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3fbc006e-9427-30ae-91a3-d560d3ef35fd | -21.31078 | -43.89071 | 2025-09-10 04:46:00 | NPP-375D | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a147090c-70f2-3395-ab6c-f70aa75f9202 | -23.35591 | -47.20359 | 2025-09-10 04:46:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 770c4694-d1a6-3ca4-9ea7-ca2c30332b31 | -20.8646 | -43.70794 | 2025-09-10 04:46:00 | NPP-375D | CARANAÍBA | MINAS GERAIS | Brasil | 3113107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ae0365ed-0c96-36ee-ab73-7e4e0b16ba5e | -22.61977 | -47.42736 | 2025-09-10 04:46:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84b55de2-bd25-3289-9c99-a967a87a5ae8 | -20.1612 | -47.70023 | 2025-09-10 04:46:00 | NPP-375D | BURITIZAL | SÃO PAULO | Brasil | 3508207 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9e29e9d-bb79-36d2-ac00-1eb56327152a | -20.00573 | -47.61983 | 2025-09-10 04:46:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ecedb09-7d5f-32f2-ae03-cdd8a6d1f9c1 | -20.01164 | -47.63675 | 2025-09-10 04:46:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9a8c741b-ecd3-3a8b-a848-34612c6d1695 | -20.05903 | -47.53417 | 2025-09-10 04:46:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f5a465a-8492-3ef4-a7b0-c0bb118e3042 | -23.03281 | -50.10291 | 2025-09-10 04:46:00 | NPP-375D | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 9a490d1d-1e80-3ced-a64b-970665ea8c43 | -20.01237 | -47.63116 | 2025-09-10 04:46:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 04f34c28-e20d-3408-9568-5d7b839a0cca | -23.24976 | -45.97497 | 2025-09-10 04:46:00 | NPP-375D | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 16b9a4cf-0148-3ae6-b452-b88705b5f1d4 | -20.00834 | -47.63097 | 2025-09-10 04:46:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b9837de5-ae61-3681-ab04-4bb1e94693b9 | -21.12209 | -42.91621 | 2025-09-10 04:46:00 | NPP-375D | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1f9baa58-2fe5-3c6a-9e49-fc43133e5d16 | -19.99928 | -47.60695 | 2025-09-10 04:46:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8962db18-13c0-357d-9d48-2c12676a9ac3 | -20.06507 | -47.5395 | 2025-09-10 04:46:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d7a55c7-0faf-36e4-a73a-3be1447b7d33 | -23.02859 | -50.10675 | 2025-09-10 04:46:00 | NPP-375D | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| ee40bda5-b8c1-3978-b5ac-11af652663cf | -20.06837 | -47.54542 | 2025-09-10 04:46:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba251c1e-a7f5-3a0b-9c48-84c34050caed | -20.01863 | -47.76798 | 2025-09-10 04:46:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 663592c8-d131-39b6-9555-2ff980ebcfbf | -23.32207 | -46.87756 | 2025-09-10 04:46:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6d55edce-2880-3abe-bad1-0d92d3af6714 | -23.40528 | -47.26244 | 2025-09-10 04:46:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 9e5e57b4-60b2-3233-b4b6-475a3c7dd4ab | -24.1858 | -50.96436 | 2025-09-10 04:46:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 84ece1f3-8685-3fc6-a236-16e3086b1572 | -23.0322 | -50.10734 | 2025-09-10 04:46:00 | NPP-375D | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 74caf764-bbe9-3fc7-ac00-0d22587e8db5 | -20.45631 | -43.95405 | 2025-09-10 04:46:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.1 |
| 27a32e2a-8e5f-3df9-af60-63d476a3c523 | -23.14136 | -48.26257 | 2025-09-10 04:46:00 | NPP-375D | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f579d2a2-e48c-3abe-a8da-5cf2b18f3552 | -21.30599 | -43.8866 | 2025-09-10 04:46:00 | NPP-375D | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1ada73f2-9922-3090-8383-91d72ac47ab9 | -19.9978 | -47.61847 | 2025-09-10 04:46:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38ca0c78-5e37-348a-a695-8dd0bbb1dd10 | -19.99854 | -47.61269 | 2025-09-10 04:46:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e458797-a051-307d-a143-fb1ead4b4209 | -20.70779 | -46.05746 | 2025-09-10 04:46:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 188bbbd1-c6f6-3759-b35c-786756df9db9 | -23.40952 | -47.26315 | 2025-09-10 04:46:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 307c3370-c99f-31fd-bcdb-f55f86d5ff73 | -22.15258 | -43.22654 | 2025-09-10 04:46:00 | NPP-375D | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| da831e9e-625a-3abe-bed8-17112beffdea | -20.00905 | -47.62553 | 2025-09-10 04:46:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8334cb78-0df5-3602-961d-5a481b66f869 | -22.5854 | -46.71996 | 2025-09-10 04:46:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| faa68c45-3249-385e-ba10-5cfd0f3db9ed | -20.55357 | -47.62363 | 2025-09-10 04:46:00 | NPP-375D | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d2c1aec4-58d6-3179-83a5-4973a6518e90 | -20.06906 | -47.54015 | 2025-09-10 04:46:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4aa4b97b-9bdb-3dc5-ba39-f2ba81eb70e6 | -20.51872 | -47.64085 | 2025-09-10 04:46:00 | NPP-375D | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ecd09999-56cb-36e7-97a8-c8d5780aecd8 | -21.18596 | -47.30603 | 2025-09-10 04:46:00 | NPP-375D | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 06396e7c-d022-35ff-b049-8a3b8f1a426b | -20.02107 | -47.62664 | 2025-09-10 04:46:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25a3c98d-15b9-33f7-aec0-52c154b206f1 | -22.57227 | -48.55894 | 2025-09-10 04:46:00 | NPP-375D | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| db3ab1e7-8e41-30d4-93d3-eadbb3dca9fd | -23.38849 | -45.96647 | 2025-09-10 04:46:00 | NPP-375D | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 41656f91-937c-3810-a113-2082b16f4c6e | -22.82746 | -46.43349 | 2025-09-10 04:46:00 | NPP-375D | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e5e5cf92-903a-38bd-8eb8-ebd06584d487 | -19.93685 | -49.26149 | 2025-09-10 04:46:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9dfa8b10-dbfa-3cb2-838c-212e04a18cff | -21.1199 | -47.73265 | 2025-09-10 04:46:00 | NPP-375D | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 39336225-129f-30b3-ae06-44ac3342789c | -20.52482 | -47.62497 | 2025-09-10 04:46:00 | NPP-375D | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3b2db2e-6f77-3f6f-b5d7-572d76d72f7d | -19.9508 | -49.26809 | 2025-09-10 04:46:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fe17cdb1-d1a9-34b4-bdd7-f1b9b16832b6 | -23.40759 | -47.26466 | 2025-09-10 04:46:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.1 |
| ee05f56d-6142-356b-9bdd-234430bdddb2 | -21.02616 | -48.41888 | 2025-09-10 04:46:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| adbfe421-8efe-3df4-9b58-7784f6050c8f | -20.08466 | -47.35939 | 2025-09-10 04:46:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac750401-8fb6-38b8-b226-8f63d6c1ef2f | -22.61512 | -47.43071 | 2025-09-10 04:46:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 100b05de-92d3-3250-9615-4a5f9561ff5d | -23.03343 | -50.09846 | 2025-09-10 04:46:00 | NPP-375D | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 1be681cc-a5bf-3d41-87e0-f99467234b3e | -21.00231 | -46.05857 | 2025-09-10 04:46:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 86efa83c-c879-35bd-ba34-19acdbcff990 | -21.77859 | -45.56421 | 2025-09-10 04:46:00 | NPP-375D | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 274a2aac-9907-3e53-9de6-2db05c097acf | -22.6156 | -47.42676 | 2025-09-10 04:46:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 353f3152-ea92-383b-b858-8cbff11efae8 | -20.45697 | -43.94799 | 2025-09-10 04:46:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.2 |
| 999ed096-e946-32c8-bf90-1e118e035cae | -21.31629 | -43.88793 | 2025-09-10 04:46:00 | NPP-375D | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bb6bedb4-4b09-3cf1-af17-b8c49beb6057 | -20.15965 | -47.6987 | 2025-09-10 04:46:00 | NPP-375D | BURITIZAL | SÃO PAULO | Brasil | 3508207 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4c25381-c240-32a3-9eb0-bcd767aa7f7e | -20.462 | -43.94905 | 2025-09-10 04:46:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.2 |
| 8555573e-2e16-3da6-909c-22e2c654e87d | -22.26822 | -42.76997 | 2025-09-10 04:46:00 | NPP-375D | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f3321efb-394b-3c24-b87d-7b9909134513 | -21.18643 | -47.30213 | 2025-09-10 04:46:00 | NPP-375D | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 79b3cf1c-0f35-3450-82ba-c8b1ee5ac2d9 | -23.49654 | -47.20842 | 2025-09-10 04:46:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 60b2cad2-b0db-36ed-86f6-e874262c7b42 | -23.29633 | -45.47701 | 2025-09-10 04:46:00 | NPP-375D | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 89b782dd-fc13-35b6-bc36-2a059dff5b40 | -20.28531 | -46.24682 | 2025-09-10 04:46:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c0e28f82-e1d6-39dc-8650-e2708f1899ec | -19.34715 | -56.70686 | 2025-09-10 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1d824170-ae83-3f26-96d8-61c1f8aa395f | -21.57936 | -44.01438 | 2025-09-10 04:46:00 | NPP-375D | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9760541d-e203-35f3-9576-b11348400d99 | -20.45573 | -43.95942 | 2025-09-10 04:46:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.1 |
| f25c74fb-b591-3fcb-b540-bf2a36898eac | -20.00251 | -47.61338 | 2025-09-10 04:46:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d18a3f22-ab57-30c5-882b-17bd0cd3ad8a | -20.00724 | -47.60817 | 2025-09-10 04:46:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 918ff010-3a00-3dea-aeb4-ba5c025bc1a3 | -23.70213 | -51.786 | 2025-09-10 04:46:00 | NPP-375D | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 297ee074-b3ab-3399-bd29-36b264063051 | -19.93624 | -49.26595 | 2025-09-10 04:46:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9f68989e-4f67-3e65-8b02-53e24fe685bf | -19.95019 | -49.2725 | 2025-09-10 04:46:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6e19f1a0-6bcf-3371-af5d-ac3dbaff3588 | -20.28478 | -46.25124 | 2025-09-10 04:46:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 513a658b-c186-3c7a-adda-7df1348221f6 | -22.26787 | -42.77369 | 2025-09-10 04:46:00 | NPP-375D | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 56fae441-5612-3aec-8833-6865c819b0bf | -23.24858 | -45.9764 | 2025-09-10 04:46:00 | NPP-375D | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3ef2c8af-ea37-3f8e-9460-1eaa47f75a14 | -19.99705 | -47.62421 | 2025-09-10 04:46:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5b0c1e5-62c5-38a4-a596-9129cf8e6b35 | -22.60057 | -49.54123 | 2025-09-10 04:46:00 | NPP-375D | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 39a85684-53e7-3746-a675-66a5bb004215 | -23.29629 | -45.47598 | 2025-09-10 04:46:00 | NPP-375D | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 846e1de3-18e4-34c1-ab5d-e8600fe6b832 | -21.23421 | -49.87999 | 2025-09-10 04:46:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 60542a7e-c2ce-353d-934e-57c34d4d61fa | -20.52273 | -47.64132 | 2025-09-10 04:46:00 | NPP-375D | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df6313a3-f6f4-324f-a8e9-73826ebf5aee | -23.97606 | -46.47158 | 2025-09-10 04:46:00 | NPP-375D | SÃO VICENTE | SÃO PAULO | Brasil | 3551009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e85864b5-b29a-3522-a44a-58d12e407604 | -23.31828 | -46.87217 | 2025-09-10 04:46:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6cc90c47-649e-372d-b0c3-c002bf245b16 | -21.32146 | -43.88837 | 2025-09-10 04:46:00 | NPP-375D | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| c1c1dd6c-bf09-3491-8a2a-d49012c74239 | -19.9369 | -49.26385 | 2025-09-10 04:46:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 51fc1d1c-316b-3ca5-bd2a-ca9f39542d0a | -20.07308 | -47.54061 | 2025-09-10 04:46:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b7dee1d-3882-3fd3-9735-b692306dc908 | -21.40059 | -44.27198 | 2025-09-10 04:46:00 | NPP-375D | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 1c2243df-51d7-3719-a99a-73d6aca015b3 | -22.87341 | -48.1333 | 2025-09-10 04:46:00 | NPP-375D | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README83.md)

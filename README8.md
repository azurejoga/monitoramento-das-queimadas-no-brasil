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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 143ecd66-320b-3248-8c48-d8a8bbc0345a | -13.4228 | -46.8484 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6a943792-f4aa-370c-a229-173bde9db31c | -11.2828 | -43.301102 | 2025-08-28 00:51:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| db468410-afde-3e48-8d56-bafd0a964606 | -15.6273 | -52.735699 | 2025-08-28 00:51:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1d493b11-8367-383d-97f1-0b215c4a6f8b | -7.3478 | -59.6255 | 2025-08-28 00:51:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e2a65a5f-ae6a-31fe-be6c-bf48cfd8e079 | -13.0833 | -46.334499 | 2025-08-28 00:51:00 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 765be760-f6d2-345d-a1e2-8acaf3668fc5 | -4.2915 | -40.944698 | 2025-08-28 00:51:00 | METOP-C | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 848ad1fa-4b72-3a11-8225-796b7fe50d3a | -13.3884 | -51.7472 | 2025-08-28 00:51:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a28652ec-d4be-3382-aceb-2803d0de0be8 | -12.7084 | -48.1656 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f8e0623c-1c27-37b9-bb3d-d88b3dd08147 | -13.6682 | -46.8806 | 2025-08-28 00:51:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 86e6f77a-58b8-3949-84f3-23d5733b8906 | -11.3228 | -43.542702 | 2025-08-28 00:51:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ccc8cf2c-7447-3f14-a99e-31fe0b8bc845 | -13.0853 | -46.342899 | 2025-08-28 00:51:00 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| db38552c-fda9-3d0e-aa2e-cd96c2ee26c6 | -12.4149 | -47.791901 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 80dff1ce-fdec-3673-bf4b-c5b562ec8c74 | -9.1628 | -59.537701 | 2025-08-28 00:51:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fbceffd8-0e59-39fd-8568-9db9e064c6c1 | -12.7965 | -48.1446 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 411da8de-2dc5-3617-aa0f-adc37733ce26 | -13.741 | -51.905998 | 2025-08-28 00:51:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 09dcc018-349e-37ff-a1db-b56037e89411 | -9.6642 | -48.309101 | 2025-08-28 00:51:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 374302ce-8d59-33c1-bc00-b47ca9cddabb | -11.8392 | -46.797501 | 2025-08-28 00:51:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2432a7ce-dbbd-3bb4-b6c5-4c1a1128eaa4 | -10.5351 | -46.703999 | 2025-08-28 00:51:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 88a5df8a-9ef6-3760-bfa4-89c7763367b4 | -9.6625 | -48.301601 | 2025-08-28 00:51:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3bf88f80-444e-3314-b382-9b054a463ba0 | -9.3189 | -57.688499 | 2025-08-28 00:51:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 70244e7c-696e-3ed5-91f7-e6e33e846925 | -10.7072 | -47.079498 | 2025-08-28 00:51:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 353b85b6-1b17-3496-a826-89759e8a6772 | -7.4187 | -40.076199 | 2025-08-28 00:51:00 | METOP-C | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 75ef2cfb-3c19-3aa9-b55e-fa82cec25d69 | -13.0813 | -46.326099 | 2025-08-28 00:51:00 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7c5a5883-190f-3bff-9549-28820853f107 | -6.1683 | -44.062901 | 2025-08-28 00:51:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0ab02e4a-319e-3650-9e18-7f17a21ed307 | -5.3211 | -55.875801 | 2025-08-28 00:51:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bc25086-af17-3656-a719-cfe9e99c9564 | -21.1418 | -45.896099 | 2025-08-28 00:51:00 | METOP-C | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 05170e4e-f9ca-32d2-8246-ece39144c7c6 | -19.121 | -44.0243 | 2025-08-28 00:51:00 | METOP-C | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0b5e5f96-bd37-3002-9151-1ef37ac590c6 | -10.4953 | -51.5881 | 2025-08-28 00:51:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 49810fac-78d8-3ba8-9993-a76cf64558b8 | -9.4091 | -48.2341 | 2025-08-28 00:51:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8883043d-991c-3a77-b070-065f65d7d3a5 | -9.7696 | -49.880001 | 2025-08-28 00:51:00 | METOP-C | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d8e43c5a-38c7-3d31-895d-6881f8ec54c9 | -11.564 | -46.3811 | 2025-08-28 00:51:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 95886809-e677-3f22-8a43-fc116b3d8714 | -16.9998 | -48.9366 | 2025-08-28 00:51:00 | METOP-C | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3838e3dd-cb9f-3a07-8114-ff1c707d0eea | -13.4852 | -46.849998 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 87e05fe2-fa9a-3a60-890a-dc945f31d18d | -10.5388 | -46.6759 | 2025-08-28 00:51:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e2a69e8e-7baf-3182-a3ac-dacc1732a390 | -9.6398 | -49.763699 | 2025-08-28 00:51:00 | METOP-C | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9038f28e-7756-3f08-a19d-ebcaf87bcaf9 | -6.8846 | -43.624699 | 2025-08-28 00:51:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f32360c9-558f-39c0-ba80-273d6c15e288 | -13.6738 | -46.904301 | 2025-08-28 00:51:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 53faeb3d-68a4-3ecd-89d0-0b81b91a84d3 | -4.8043 | -47.2677 | 2025-08-28 00:51:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7464f0d8-3d42-3f2e-a760-cff61df193a3 | -13.4638 | -46.846802 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b61ab2fa-0a4a-3755-977b-7237c9489482 | -13.1823 | -45.287498 | 2025-08-28 00:51:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8d2d5e7c-5286-35bf-8718-6b579187a6e6 | -3.2327 | -43.441601 | 2025-08-28 00:51:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f32c8041-9ac6-3ccf-84d0-d60b0e61ac4a | -13.4736 | -46.844398 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6749b264-d918-3bf4-b294-de2c3d1b650c | -12.6808 | -48.179798 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b83c9206-b6a6-35c5-ad4a-8a07ce81234b | -12.8097 | -48.156898 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4d642319-59b0-3e60-93f5-f20347824707 | -9.4916 | -51.9333 | 2025-08-28 00:51:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7777d079-1d1e-37de-a1dd-2442c3f70529 | -12.7901 | -48.161499 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ccc775d2-3315-3c73-b984-4b53d39d81f8 | -12.4353 | -45.961899 | 2025-08-28 00:51:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4e4297ca-3d06-3b45-be82-589aaa3e3bb0 | -13.454 | -46.849201 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 10cd19bd-e242-3e31-8489-7ed54f8c2467 | -6.8772 | -43.594799 | 2025-08-28 00:51:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| db8f5dae-09db-3f29-8daf-f6759e362174 | -21.148001 | -46.966801 | 2025-08-28 00:51:00 | METOP-C | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6b772772-5054-3214-8fd1-b81965e9d45f | -11.7981 | -46.798698 | 2025-08-28 00:51:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e249f4bc-a2c4-345a-a15d-82ecf18408a7 | -13.5333 | -46.922001 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 232e31ff-59a3-3a2e-901d-059e8f8ce2cb | -17.5457 | -46.617599 | 2025-08-28 00:51:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9363e13b-a5b7-39ab-af48-67eb81173c76 | -6.8615 | -43.614498 | 2025-08-28 00:51:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 855c7785-17a9-387e-abf7-b024780311a4 | -12.7884 | -48.154202 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0fbc7ea7-dc76-3698-b11d-bf0e55338c4c | -21.684999 | -49.058998 | 2025-08-28 00:51:00 | METOP-C | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bbe3a354-96c2-3b29-863a-df0afb44b4cd | -13.1921 | -45.285099 | 2025-08-28 00:51:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 42ff8f21-d40d-3700-a108-cadf8907f69c | -10.8164 | -60.751999 | 2025-08-28 00:51:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 65b79d05-bd48-3bac-a7e3-dceb09312edd | -20.2558 | -42.007099 | 2025-08-28 00:51:00 | METOP-C | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 465dcb70-bc1c-3813-b276-ddc07e205798 | -12.808 | -48.149601 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7b0a4dee-5c0f-39ea-b53b-a6d0aa6ab079 | -11.2246 | -55.052299 | 2025-08-28 00:51:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9c64da7e-8118-379a-84b2-2b49df0fb016 | -13.9927 | -46.330799 | 2025-08-28 00:51:00 | METOP-C | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 80780cbb-a334-3cb8-ad18-76e38ce20571 | -13.4307 | -46.8381 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a097ac16-7cae-3e24-9c84-8b411a9cb779 | -12.6888 | -48.1702 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5dc9e652-2c9c-3ba7-84f8-2ce215fd3874 | -4.7999 | -47.249001 | 2025-08-28 00:51:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 67ced814-c108-3ba8-9d09-f2bc8085c909 | -21.149599 | -46.974201 | 2025-08-28 00:51:00 | METOP-C | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6578036b-ede4-380f-9ad0-dc1ce94a3201 | -3.7939 | -45.052898 | 2025-08-28 00:51:00 | METOP-C | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3d830cec-0251-3303-b25f-66eb42be7a74 | -3.2424 | -43.439301 | 2025-08-28 00:51:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7a60278a-8b10-34df-99b9-41026c887eb2 | -13.4778 | -46.993698 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| db81369b-a462-362b-805d-fe20cad54b69 | -12.7803 | -48.163898 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 86a37f9d-1ff0-3886-9143-e48677089ad5 | -14.1416 | -45.4016 | 2025-08-28 00:51:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 368e5299-e5d8-33f6-8150-1c85f0bf63b7 | -18.0609 | -45.1651 | 2025-08-28 00:51:00 | METOP-C | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 81ef8335-20be-3c49-889c-aac9d6e4ba6b | -13.1898 | -45.2756 | 2025-08-28 00:51:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3d7b283d-6590-3c4a-bd65-b6557c94832d | -23.7577 | -51.889099 | 2025-08-28 00:51:00 | METOP-C | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 512f167b-58b6-3d90-9a2c-b3e96f70ac82 | -10.4704 | -57.953201 | 2025-08-28 00:51:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| de728e97-5427-3245-85c1-b66839ac17f9 | -13.6088 | -48.2187 | 2025-08-28 00:51:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| eb8d67d1-9726-3b66-814b-cd83d0e29d9b | -12.7952 | -48.1833 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ac814747-9322-393d-829c-cc62f5d097ce | -17.819599 | -44.510899 | 2025-08-28 00:51:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a3636fed-190a-376d-aeb6-be4c57c7c6fb | -13.4247 | -46.8564 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c3123ae5-6b8a-3284-97f1-d344436202f7 | -9.6162 | -40.348 | 2025-08-28 00:51:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 88580f82-89be-3aa4-9fe2-51053d9656d5 | -13.7329 | -51.916 | 2025-08-28 00:51:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 176accc5-67aa-315c-8b8a-b02fbc289172 | -15.6552 | -49.7467 | 2025-08-28 00:51:00 | METOP-C | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 19dc8aa0-9509-3292-b287-c833feca707e | -17.0014 | -48.943699 | 2025-08-28 00:51:00 | METOP-C | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cc1f8d92-4428-3b25-951b-92c0ab0b074c | -13.5491 | -46.901402 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| df62fe92-2edb-306e-a3ca-b9a5cada52ca | -13.4429 | -46.977299 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 634b4e55-d83c-3eac-916b-f0de132a28e8 | -9.4169 | -60.542099 | 2025-08-28 00:51:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 51d8d551-2dc0-34b8-806a-587d22825ca1 | -11.3196 | -43.529701 | 2025-08-28 00:51:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5d641407-d320-3c1e-bf1a-5f347a34b796 | -6.5745 | -47.379799 | 2025-08-28 00:51:00 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 92ffeef3-81be-3218-8468-facfccee05d5 | -11.8099 | -46.804699 | 2025-08-28 00:51:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fca58593-00c1-3c58-954b-488da1f577d4 | -14.5748 | -52.0154 | 2025-08-28 00:51:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4359e680-0830-3226-a530-988acb82639c | -18.546499 | -43.881901 | 2025-08-28 00:51:00 | METOP-C | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6dd2b600-c45c-360f-af7e-c454739dfa1e | -12.9287 | -46.3368 | 2025-08-28 00:51:00 | METOP-C | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7cf3639e-d2e1-31ca-a95d-a499ed4dd1f1 | -18.4617 | -49.694401 | 2025-08-28 00:51:00 | METOP-C | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7b09faa8-818d-32fa-ae73-4880eff84de5 | -8.4586 | -43.6954 | 2025-08-28 00:51:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8279cc1d-beda-3311-bda8-c6c55767ec46 | -3.7589 | -54.818501 | 2025-08-28 00:51:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c941928-3c91-3cd6-b5c8-ec8473d8d60c | -15.6137 | -52.7197 | 2025-08-28 00:51:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fdc391c9-2e0f-31ae-9424-3b709dd2194b | -10.5408 | -46.684502 | 2025-08-28 00:51:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 30557437-f3ec-3615-ad4b-cce3534f8e98 | -9.3976 | -60.546001 | 2025-08-28 00:51:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4ae88f38-815c-3641-8a68-16d195e34a92 | -13.0871 | -46.306801 | 2025-08-28 00:51:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5b35909e-14a6-3434-8cd5-4123c7e4ef09 | -17.7738 | -44.493401 | 2025-08-28 00:51:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README9.md)

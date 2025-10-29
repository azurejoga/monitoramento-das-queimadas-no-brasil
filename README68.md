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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c71c6aa9-7f29-36ec-b5ab-3e46a32b2e96 | -13.64602 | -47.03168 | 2025-10-29 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68c34401-b934-35cf-99e3-58fe3f4e7480 | -13.0497 | -43.82136 | 2025-10-29 04:46:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b64c613f-7065-369c-abfa-db73253fbd5a | -10.7421 | -44.75877 | 2025-10-29 04:46:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b94749d7-5f09-3875-bf82-0908061efb88 | -10.75425 | -49.78056 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09ef9d50-ea8c-3fc0-a736-25747f05a843 | -14.99184 | -47.86772 | 2025-10-29 04:46:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2cc3b0dc-21cf-3757-acb8-f21c660ded2b | -14.32575 | -46.51814 | 2025-10-29 04:46:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72692e73-6aae-35a3-9fff-14cfa1fb762d | -14.52445 | -47.98743 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23d932fb-2ce3-3016-a5a2-a85661643c92 | -14.50021 | -47.87835 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a91347e5-052d-3ffe-928c-9ca4ccf4c700 | -10.85927 | -50.12772 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4fde7395-6090-315b-b34c-60ff46fead0c | -13.4429 | -48.62043 | 2025-10-29 04:46:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 539b7364-8698-3811-ad8f-cb7315846ac3 | -12.00076 | -46.78159 | 2025-10-29 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| df70e5d4-5e83-30c7-9d47-ca73e32e3a00 | -13.57699 | -49.60304 | 2025-10-29 04:46:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dfd4a5cb-661e-3027-869a-07c9a0385cc2 | -15.64355 | -42.91687 | 2025-10-29 04:46:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 50cfaf36-0e94-3352-b476-751377cd300f | -13.64065 | -46.47196 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cea19605-4bcd-35f6-b4a6-17afcb6f90a9 | -14.33983 | -52.56619 | 2025-10-29 04:46:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9bb7425-8132-374a-ab9a-d94ea03dfb24 | -10.7666 | -44.74325 | 2025-10-29 04:46:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4bf5dccd-e52d-36f4-bf5f-851ded653c85 | -14.51914 | -47.99701 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3f56540-a79b-3c88-a416-9cf627c13b03 | -13.6412 | -46.46787 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7fb3c0d-0d9d-39ca-b3bc-68995344b197 | -13.56327 | -49.57181 | 2025-10-29 04:46:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 393ddcd2-26ff-3a64-b421-1d8e33393b5c | -13.34313 | -46.34932 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2821fcdf-53ad-38af-9d73-7a18704900e8 | -13.67 | -47.18582 | 2025-10-29 04:46:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 838ffdb5-c9da-3a7a-9342-7b57e01756b4 | -14.61281 | -48.39541 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 039677ff-f69c-3163-b8db-b10f79ff4533 | -13.37301 | -47.41873 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a31a0234-1484-3680-b827-6c0c3ded6587 | -10.98841 | -47.85779 | 2025-10-29 04:46:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4326dee-ec44-3375-8cd8-c0a97545ffbe | -14.13993 | -44.14643 | 2025-10-29 04:46:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db29d064-37f7-334e-8d89-1da3a1e97d12 | -13.63394 | -46.52111 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 098c60fb-5c76-3b51-bae1-bb4d3704548b | -14.60827 | -48.39986 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af073fbe-533f-32ef-b906-09e0ed8cffd6 | -10.95769 | -47.61577 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 6f16c416-1027-3b04-95a5-1aa8cc02ade0 | -14.27845 | -47.31875 | 2025-10-29 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a887e971-e8cb-3123-81cc-89601f72dfbb | -9.2305 | -46.36152 | 2025-10-29 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a056bb0a-13df-3019-9b43-b74a919313ef | -12.52887 | -47.54113 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f09f687-423d-3619-b8a9-e0f8b132358f | -13.56935 | -47.16345 | 2025-10-29 04:46:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0155b66f-f8c8-358e-aaa5-a8d8c5e6fa63 | -13.57997 | -49.60759 | 2025-10-29 04:46:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a84eb53f-f447-3c53-bf2c-cba098b61e14 | -13.56116 | -47.34844 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7bb70b16-b9da-38fc-a562-a5ab228241ce | -14.75149 | -49.66267 | 2025-10-29 04:46:00 | NOAA-20 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0d107b75-7240-3a62-86e5-42b89a8b5966 | -10.50094 | -47.7302 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b125bbe-4772-3f3a-9d14-a4787432937c | -13.63253 | -46.51839 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 76bdc408-2a03-38d2-8733-4e214b32264c | -10.97678 | -50.25196 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bcfeaad4-9071-397b-9448-971e1d046452 | -13.55614 | -47.32427 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7581b114-ce03-3a8a-92c4-9bd9282ad2f8 | -12.20921 | -47.90525 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8dfbae88-f3a6-3fa0-b991-ce7eaaf4cbd6 | -15.16025 | -47.23604 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5387c74-e70b-3110-b504-8fa2f932b3f0 | -10.85749 | -50.09307 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| fab6e796-436a-3b25-aaee-46112614fd42 | -10.85589 | -47.89318 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| db455585-a2bf-35cf-bcc4-6e4828cc52d6 | -12.35997 | -50.15498 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2f0628e4-9ad0-3d96-a23e-569165a25bc7 | -13.41113 | -47.38132 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0909a50c-0642-3834-8b3f-ed2c199fb387 | -10.70381 | -48.00847 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b7ebd3b-f589-3994-b1f7-d3d7447f3b32 | -12.35594 | -50.15828 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5dc0418d-ad5c-3d2c-ba05-2edf1ea05df6 | -12.52813 | -47.54633 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d871572c-4b67-393b-9dfc-91bb16d66581 | -10.85712 | -50.0932 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 843d3db5-fd19-3834-a2a2-f66c267b885b | -13.24782 | -48.00344 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a37cbde-f130-3afb-8d21-12c30cffed80 | -12.71329 | -46.31499 | 2025-10-29 04:46:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a3b81b1b-b9fe-3756-aa08-c9b80a83a9af | -9.91189 | -50.49926 | 2025-10-29 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2928473-9bd4-316b-83f3-6b9229ed3bd2 | -10.5061 | -47.72137 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a03f7fb3-0935-3154-a53c-a541fb5f6393 | -10.61465 | -49.61041 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f4443f47-8ee3-36aa-a6dc-8d7360bd72fc | -10.51751 | -47.72303 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ae74d1e-cd28-3f35-8c96-f080694db27c | -13.63146 | -46.52665 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0f2fc834-70e2-3f37-8874-d26f89ce0367 | -10.64315 | -48.00434 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1d846411-f667-3c06-a524-12963bb9fa44 | -10.92893 | -47.59677 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13586c33-c7c5-385c-a4d5-5e8578649380 | -12.65736 | -52.61628 | 2025-10-29 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9a7254c-5e20-3b13-862f-2c0e69ed010d | -10.76957 | -44.08522 | 2025-10-29 04:46:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 838ae1e7-6661-379a-a531-28a068d75b53 | -13.58231 | -49.59149 | 2025-10-29 04:46:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 945520b8-46d9-3d85-95c7-f80435e2d07a | -10.90515 | -49.47444 | 2025-10-29 04:46:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1b05c62-5fac-33fd-aab5-4773d01a2ad6 | -10.60436 | -49.61813 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cb027c3b-2a51-3d2a-b4ec-54701ad1a3bc | -12.68957 | -48.4358 | 2025-10-29 04:46:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90636575-3408-382c-a851-4801b42c18b1 | -13.69652 | -47.68387 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f2c6fe1-d559-3021-9b26-055d0888f2ea | -11.10999 | -44.01688 | 2025-10-29 04:46:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 835dabd2-45f8-313b-9bc0-bfd19d224ba2 | -11.78801 | -44.16708 | 2025-10-29 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7abb158e-3bbf-36a8-98f1-6477c23059c4 | -12.00026 | -46.78531 | 2025-10-29 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 3a2dead7-9f01-3090-abe6-fafe3c2b6d09 | -10.76665 | -47.89715 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a2fa627d-55d6-368f-bb3a-7695ef8af1d8 | -13.91288 | -48.46296 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42191840-38c1-3142-9a9c-1214358a2200 | -9.5403 | -46.92324 | 2025-10-29 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a7d6feff-2d29-34c9-82d1-6fe0b07339cf | -13.63622 | -46.48971 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60f30b59-8210-3d19-a094-e145f983804a | -12.52718 | -47.5475 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71244859-db40-3f06-830c-52a5097bb5cf | -10.63986 | -52.18259 | 2025-10-29 04:46:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85bc4f7d-80ab-3625-9379-204404eb18c2 | -13.17728 | -48.45488 | 2025-10-29 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d53a52d0-e4c8-3a58-b829-b246112bd4ec | -9.27224 | -46.38993 | 2025-10-29 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fbba05d1-aa5d-3dd9-a021-d2f0b06661b8 | -13.31926 | -47.45181 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b628dbe0-14fd-3b0e-80d6-3bccf6cd3b20 | -13.86563 | -48.49943 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 056d8bd0-9883-3d72-a679-ee9981248ff0 | -13.88265 | -48.46143 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49e8f095-98c1-37f1-bd12-070a30106ae7 | -14.2762 | -47.30476 | 2025-10-29 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f4983d8b-6122-30fe-8a06-0fab3430f88f | -12.00796 | -46.75951 | 2025-10-29 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f365c957-d2d9-3bcd-9d80-7b68e8cc05f9 | -13.66622 | -47.63904 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9825863-9311-348d-94b6-e0c66b93cc52 | -10.56961 | -49.84186 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 95f46177-1a5c-3a34-be3d-a3ebacc4290f | -10.65066 | -48.00535 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 81ccea50-c92e-3dee-8555-d88412b63386 | -9.57022 | -44.71542 | 2025-10-29 04:46:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e9a823d-55d4-3e95-8277-fd21bfaef535 | -10.85286 | -48.64276 | 2025-10-29 04:46:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9f476ebb-1a8c-30c2-ab7b-4aaf4281f7e0 | -12.39663 | -46.65152 | 2025-10-29 04:46:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be5dcc16-c53b-32a0-8650-6b5958c367e7 | -11.99614 | -46.78473 | 2025-10-29 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 8be13686-5047-366c-bd5b-4260ca374e32 | -13.04479 | -48.46563 | 2025-10-29 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 45640c7b-0a93-3242-a70c-38e78cd81579 | -13.68584 | -47.19257 | 2025-10-29 04:46:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| db8e37a3-a353-3fdc-a933-ab570bb636d9 | -9.74057 | -47.75301 | 2025-10-29 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6ea630c-a6f8-31b0-882e-3b3b7aeb75d7 | -13.52576 | -47.33477 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1c4f6c31-c059-3206-b19f-3cebe8a0e946 | -10.85325 | -48.64566 | 2025-10-29 04:46:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d01c9c30-3fc6-3363-a4f8-4aa71b7ea93c | -13.60644 | -48.41994 | 2025-10-29 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39d360cc-772a-3124-b6bc-23a6fb797886 | -11.40711 | -51.38616 | 2025-10-29 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6d1ba448-8817-3a3d-8f6e-662f487d90cc | -9.78939 | -47.60414 | 2025-10-29 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f577c75-5157-3357-a425-71ef6ff69859 | -12.85584 | -48.62513 | 2025-10-29 04:46:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0211f042-2e34-31e4-85da-69e94a24ea3e | -9.90447 | -51.22282 | 2025-10-29 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a22dcbdd-9308-357f-b7f0-da63eb8ea57f | -13.64365 | -46.51409 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af9b00d0-f8f3-339b-98e8-91da2a3a2cfc | -10.88148 | -45.07233 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README69.md)

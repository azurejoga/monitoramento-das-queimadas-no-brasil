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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1547f089-dc57-3c7e-a13a-9db308dc000d | -15.46287 | -46.14912 | 2026-09-29 05:14:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0268194-2b41-3265-8012-fd2c061c2712 | -21.06136 | -48.8431 | 2026-09-29 05:14:00 | NOAA-20 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 52b1edbb-a45d-3067-8bab-57520734e0f3 | -15.51148 | -56.73869 | 2026-09-29 05:14:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f481c8eb-ee9b-36b9-b6f3-4db1b3beb186 | -19.90909 | -54.58767 | 2026-09-29 05:14:00 | NOAA-20 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08d55f38-48bc-3859-b709-b1c58488ac91 | -15.08963 | -48.33168 | 2026-09-29 05:14:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 34501686-8661-3256-84ac-ff82c6d03785 | -14.52467 | -52.48747 | 2026-09-29 05:14:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e8d4ea39-fbad-37cd-a30c-af744d4f457c | -18.57561 | -48.41732 | 2026-09-29 05:14:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 07f859ef-0a9e-38b4-98b1-439ae0d413f0 | -15.2118 | -46.16966 | 2026-09-29 05:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b58aac44-5740-3893-9921-df66a6452e52 | -18.10806 | -44.3578 | 2026-09-29 05:14:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9901c093-8eba-3b65-8102-5599b5144a46 | -15.21426 | -46.16621 | 2026-09-29 05:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a33319aa-743c-3cd7-b12e-96b6a49e4e8b | -20.21096 | -48.56734 | 2026-09-29 05:14:00 | NOAA-20 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0e68fd2-b314-3637-930c-fb0a30c680ad | -15.38739 | -47.92524 | 2026-09-29 05:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f06f031e-592d-3fe0-a509-e26fc8c6aa8e | -15.46426 | -46.13587 | 2026-09-29 05:14:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75e71ee0-1cf9-3be4-9bae-b236f0c432a9 | -14.96395 | -47.54369 | 2026-09-29 05:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf061528-7991-3eae-a25e-d938cb28f869 | -14.2673 | -57.67166 | 2026-09-29 05:14:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90260ce2-1255-380a-a442-e62f9b7b6571 | -20.21667 | -48.56805 | 2026-09-29 05:14:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b08f6ac-be9c-3a8e-b63b-a6b2a76a1319 | -15.00939 | -51.40866 | 2026-09-29 05:14:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dfc91b13-e185-3de9-b37e-37b110daebd3 | -18.56349 | -48.42394 | 2026-09-29 05:14:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 107ea10e-39e8-311e-8207-6c36dd753cf0 | -16.33204 | -47.69913 | 2026-09-29 05:14:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0bfdad6e-1c8e-35cd-9a01-940bca8f2d91 | -20.83278 | -57.68718 | 2026-09-29 05:14:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 7c6ae968-10c3-3ef8-a3c1-30d45edaf3a3 | -15.09482 | -53.87293 | 2026-09-29 05:14:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8a721a0-8ce4-3969-8de1-e79ea867e454 | -18.10397 | -44.35842 | 2026-09-29 05:14:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21ba797c-1473-3191-b45c-70e87f654f97 | -20.82881 | -57.69048 | 2026-09-29 05:14:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 5c3ce644-269a-3f42-aff8-d640c304151b | -20.69847 | -57.95987 | 2026-09-29 05:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 5ce8898a-f424-3d27-b6ec-9fe31c3f1695 | -15.35212 | -59.14783 | 2026-09-29 05:14:00 | NOAA-20 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e5b10d4f-88c5-3fb0-a8b5-82e7f0868c97 | -18.5726 | -48.41751 | 2026-09-29 05:14:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| cff4c8a8-5db6-3f34-a447-309d691471e3 | -21.04976 | -48.87552 | 2026-09-29 05:14:00 | NOAA-20 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cb808610-6416-3af6-8667-3c6573005bef | -15.77489 | -52.45231 | 2026-09-29 05:14:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7311d830-59bc-3500-bc81-d758e902f0cc | -15.22468 | -46.18654 | 2026-09-29 05:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f4d221de-30c2-3eae-ba34-6ef84e981f53 | -18.56043 | -48.42414 | 2026-09-29 05:14:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8a4155fb-0c24-36f4-9042-c79e24aefff3 | -14.63283 | -52.13745 | 2026-09-29 05:14:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0612248b-665b-35fd-be00-1025bb9537aa | -18.57178 | -48.42512 | 2026-09-29 05:14:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 934d0ade-5cb2-32e3-8474-d5cb127ad99e | -18.6828 | -48.62772 | 2026-09-29 05:14:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4852f084-31c4-374a-8816-c747d4434b56 | -15.00278 | -47.87233 | 2026-09-29 05:14:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a24d4c37-9f6b-3f80-8a61-3819e52fa796 | -15.09414 | -53.87768 | 2026-09-29 05:14:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0c21c44-0375-3437-8fc7-2c89571ff19f | -13.50865 | -61.14288 | 2026-09-29 05:14:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12662225-1723-31ec-8f27-ce02c4f67300 | -18.56611 | -48.4246 | 2026-09-29 05:14:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8e6c7b05-cdeb-3caa-afea-5b4a45a6af0c | -18.08433 | -44.38134 | 2026-09-29 05:14:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a41f55dd-55f4-340a-881c-78516fb670eb | -21.05266 | -48.87539 | 2026-09-29 05:14:00 | NOAA-20 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 807c18f7-07e6-35e8-8562-97680e0fd95a | -21.0558 | -48.87239 | 2026-09-29 05:14:00 | NOAA-20 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 78dee937-4862-312a-aa4f-7a48b9e2d1c3 | -21.06173 | -48.83911 | 2026-09-29 05:14:00 | NOAA-20 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fef571bc-252a-3f90-9995-6b0a31b326b0 | -14.92202 | -59.39199 | 2026-09-29 05:14:00 | NOAA-20 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba3e8850-222f-3d9a-aafe-876483cb40e9 | -14.09764 | -54.29954 | 2026-09-29 05:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 94d7acf5-6b6c-3a3d-8c26-e80eb894e1ec | -15.3367 | -48.12414 | 2026-09-29 05:14:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 047ac7ad-8fe3-3836-9908-ac7abe9c6256 | -18.5657 | -48.42844 | 2026-09-29 05:14:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| eada5aef-82aa-3b49-8f40-6bfdc609321e | -15.47054 | -46.13667 | 2026-09-29 05:14:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1658a512-19d7-3afc-bcc2-0839c53b98d4 | -14.86561 | -47.99319 | 2026-09-29 05:14:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4196b76-826d-393f-b093-12a11ff4bc8d | -14.76632 | -47.15637 | 2026-09-29 05:14:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da6588aa-e322-3ec5-a2f1-fdf9facb33ec | -15.63571 | -52.69218 | 2026-09-29 05:14:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a34e3c40-1c3f-3d07-9890-a99d90703ae8 | -14.52058 | -52.48691 | 2026-09-29 05:14:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 92488eba-80b3-31c2-850e-126e4b4b7d6d | -14.1013 | -54.30009 | 2026-09-29 05:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17a5abb2-6da9-30a4-9dab-b86a3984d0f2 | -15.3887 | -47.9136 | 2026-09-29 05:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b4110dd-8ef2-3c72-898f-f676cc22511c | -18.67722 | -48.62698 | 2026-09-29 05:14:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 514dc2da-0e75-373d-9df0-484a30992c5d | -15.22518 | -46.18204 | 2026-09-29 05:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bee94d33-b187-3bc7-b82d-372542b75c93 | -18.56879 | -48.42823 | 2026-09-29 05:14:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7155323a-4fbd-3718-af5d-2a6062e1c004 | -18.09217 | -44.37421 | 2026-09-29 05:14:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4220c46-c428-3dcb-9d57-16313084ca9a | -15.21359 | -46.17229 | 2026-09-29 05:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d1c4f6db-e7f7-328e-924b-e04cec38c0c8 | -14.52108 | -52.48319 | 2026-09-29 05:14:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f026ad5-73cb-38b9-96ee-8d2f73972aae | -14.62914 | -52.13302 | 2026-09-29 05:14:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 121b053e-5c5a-36d0-9464-f42901dc5c79 | -21.05303 | -48.87141 | 2026-09-29 05:14:00 | NOAA-20 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0a3d1bb1-40ab-3b06-a878-34cda33ddeba | -15.38221 | -47.92064 | 2026-09-29 05:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b86fc92-4004-30a2-8c37-177535a8acce | -21.05016 | -48.87155 | 2026-09-29 05:14:00 | NOAA-20 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 07244ef5-8953-38fc-95e5-741a7e1e149f | -19.90523 | -54.58712 | 2026-09-29 05:14:00 | NOAA-20 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89441fa2-6b85-3b7b-80f3-0230cfdb2b32 | -19.90589 | -54.58207 | 2026-09-29 05:14:00 | NOAA-20 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd2a9834-6e11-3ccb-a3de-c9670139712d | -18.11117 | -44.35876 | 2026-09-29 05:14:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b7ecce1-61cf-38bc-b7ff-40ab1722a77d | -15.39815 | -47.93073 | 2026-09-29 05:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c83511d5-38c7-3d1d-b19f-a2157e16c453 | -14.95972 | -47.5423 | 2026-09-29 05:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bb2a3dfd-f048-3dc2-b862-a133e828a51c | -15.15966 | -46.14328 | 2026-09-29 05:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f85960b-8f5d-3b71-9ed0-bcafffe4e3de | -15.39777 | -47.93414 | 2026-09-29 05:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a95f17f9-c0a7-3443-8704-6bc7025610ce | -15.17367 | -46.13095 | 2026-09-29 05:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c2cea1a-e68e-3a8c-82d7-3e34eb37b5de | -20.09701 | -57.20358 | 2026-09-29 05:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b9263dce-9624-3575-b438-d4780b090fdd | -16.33781 | -47.69978 | 2026-09-29 05:14:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ba77011-29f2-3ca8-9c9f-21b11ec6f00a | -15.17419 | -46.12619 | 2026-09-29 05:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 299ef042-c46c-3c64-a169-96809a44d498 | -15.09861 | -53.87347 | 2026-09-29 05:14:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b25878a4-079c-34a7-8c1a-4b16ac34cc7d | -15.96112 | -52.21162 | 2026-09-29 05:14:00 | NOAA-20 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46842fc3-a466-36bf-84d7-8ff040160dd5 | -15.20732 | -46.17166 | 2026-09-29 05:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc6b9a69-b670-3084-aa60-ccfd92eca554 | -15.38966 | -47.90514 | 2026-09-29 05:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88cede25-079f-3afe-80da-62ef15b16c5f | -15.46333 | -46.14471 | 2026-09-29 05:14:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5859ddf-5ed7-34cc-ad13-6c244cd28235 | -15.08416 | -48.33126 | 2026-09-29 05:14:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 631b2888-daa7-39e3-b430-713f2360ed9a | -15.39298 | -47.92609 | 2026-09-29 05:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f355f004-6257-3216-b004-50e579f166db | -17.14073 | -47.72501 | 2026-09-29 05:14:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4be8468-3d06-319d-a2a1-0750f827f65a | -15.45708 | -46.14369 | 2026-09-29 05:14:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9624e473-3933-3a42-a707-980555ab2727 | -15.09928 | -53.86872 | 2026-09-29 05:14:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a18a61b-75bd-3d63-860a-a5edaaccb52c | -15.34224 | -48.1248 | 2026-09-29 05:14:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0a0b71c-afb0-3331-b427-024a39e8c168 | -15.4566 | -46.1482 | 2026-09-29 05:14:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a1d5c1b6-a0c9-31e9-86af-0637b0316701 | -15.22575 | -46.17694 | 2026-09-29 05:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9e3228e-0f77-3b11-9ef3-03e4e41e5a38 | -15.09347 | -53.88243 | 2026-09-29 05:14:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0d974b8-956b-361e-a246-cad662873773 | -18.56916 | -48.4245 | 2026-09-29 05:14:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3f1fac3b-5094-372b-ad27-8fd8682e4999 | -20.8322 | -57.69104 | 2026-09-29 05:14:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| cc536193-a17c-32f0-b4dd-7d879e46cb09 | -17.6546 | -46.53912 | 2026-09-29 05:14:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa2478ce-76a2-3741-a558-b1d3fd9c531d | -15.21818 | -46.16925 | 2026-09-29 05:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d044e705-e007-3936-bb9b-7ec39e4dc9e3 | -15.08376 | -48.33474 | 2026-09-29 05:14:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ae08eb2f-35b4-3cab-aecf-e7f0c7ad9cb5 | -15.39857 | -47.92704 | 2026-09-29 05:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cddebb08-a5dc-3d4e-b5e9-1e0533dde90e | -15.08294 | -48.33157 | 2026-09-29 05:14:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 382dca72-e1df-3cec-b2ef-683a4a508497 | -15.16643 | -46.13938 | 2026-09-29 05:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4675d406-a9f1-31c5-ba8d-fc29bfca9486 | -9.75902 | -36.96875 | 2026-09-29 05:33:00 | AQUA_M-M | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 24.8 |
| ecb01266-8eae-35d3-83cf-a8853ae9bce3 | 4.07499 | -59.94363 | 2026-09-29 05:53:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f0cae230-9b4b-3c6c-bcbf-aa2522bc342c | 1.69025 | -55.94613 | 2026-09-29 05:53:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eed5eb54-9001-3ecf-93a0-514ad64cd8da | 1.68744 | -55.94821 | 2026-09-29 05:53:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 843ad381-2a72-30e4-87bb-0b5ba2f8d2a0 | 1.69481 | -55.93621 | 2026-09-29 05:53:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README67.md)

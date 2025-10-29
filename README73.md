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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c57e8b49-746d-3911-84e6-1042479d354a | -10.38789 | -45.30447 | 2025-10-29 04:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea6f17b1-e22e-340a-b81b-dd189e9fca50 | -13.54167 | -47.13004 | 2025-10-29 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 39983a37-7e3c-384a-aea2-41bcf768542b | -10.94397 | -48.0356 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aace01dc-5771-3125-b54d-270c6bf9d7f5 | -13.23235 | -48.00085 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f4487e5e-89af-3d6b-9caa-add88eac2b55 | -13.34098 | -46.34804 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af182741-6644-3e09-9c03-5309277c4771 | -13.64309 | -46.51815 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1e3ace57-dac0-3a94-8ce1-c7cf31654b4a | -12.2137 | -47.90129 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 589493a8-822d-3fc4-989e-a5276eff7851 | -11.06566 | -47.53442 | 2025-10-29 04:46:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 722b4ad5-1630-3f8d-b8e4-ecb961b3dd4d | -10.20962 | -45.94891 | 2025-10-29 04:46:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0eb1f17-b6fd-330d-8c52-2d211b458538 | -11.1734 | -45.23083 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 452bf4f3-7e96-3c3b-80b2-195d65e35b93 | -12.0812 | -47.99158 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e6c87177-8a6f-37c7-87cd-6c522ec806f2 | -10.66569 | -44.80074 | 2025-10-29 04:46:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b013f25d-1186-30fa-96be-e00e446ad373 | -11.33849 | -46.06964 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb32946a-a386-35ac-9501-a66370700363 | -9.09689 | -47.81792 | 2025-10-29 04:46:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 956a02ac-b6a8-39bb-ad3d-3a3ba3662b60 | -13.56664 | -47.33854 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46c842e7-f4b0-3604-98f7-ed01007d8359 | -13.9383 | -50.33659 | 2025-10-29 04:46:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fdc0ba3a-77ad-393e-ae3b-3b5072646169 | -13.68227 | -47.18803 | 2025-10-29 04:46:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1346e0f-88d5-36db-b11a-89e9f6f49c24 | -12.36283 | -50.15934 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d73e38e-23bf-3584-926f-bbbc57e05cb6 | -10.94246 | -50.34112 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 85c7cd99-c2d0-37aa-9964-ae420a4fff82 | -14.66056 | -50.19374 | 2025-10-29 04:46:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6f8a178-8b31-3f05-9ab4-3688b1e50905 | -13.5677 | -47.33076 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ea8ca97-b869-3531-aab7-9b3a99026104 | -13.57283 | -49.60661 | 2025-10-29 04:46:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5f18eec3-f691-32b8-b59a-bf2dfb5c5333 | -10.33923 | -47.78067 | 2025-10-29 04:46:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f04b9786-4de3-30e8-b8c5-6828ac89e5ee | -12.54025 | -49.58281 | 2025-10-29 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1835d999-62ab-3c15-84a0-80b976e117f2 | -13.22672 | -47.06799 | 2025-10-29 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e7484230-2d21-3b5a-b00c-5615e82db017 | -12.0148 | -49.83942 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5367f8e-0278-3a49-9256-5722d843567d | -9.72013 | -45.40194 | 2025-10-29 04:46:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a6a004b-40db-3752-8374-1a078c6be1af | -13.91446 | -48.45629 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df59ed0e-1fd5-354b-9842-1ec62d8ab2c4 | -8.73203 | -49.76891 | 2025-10-29 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cb80842-953c-35f8-9c31-af42596e8d78 | -10.94093 | -47.623 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62232c1c-0f7b-389c-aab6-925cf540bd4e | -13.63991 | -46.50947 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9fee655f-99ef-3077-8761-fe61925f81d1 | -10.38916 | -47.11496 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b81a88b-383d-335f-9205-49fa2a4ec6f8 | -10.91213 | -50.26133 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3685e747-f328-3c94-bfb8-78454af475b4 | -14.27954 | -47.31082 | 2025-10-29 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7c065105-1749-3890-b25f-9d40dc6b568a | -15.31993 | -47.8628 | 2025-10-29 04:46:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df9d6cfe-a4eb-3bdb-95f7-33c3b1fa1798 | -13.66226 | -47.18107 | 2025-10-29 04:46:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 033cb272-3db4-3d8f-9335-33452d8bc846 | -10.85693 | -50.09681 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 0b752027-9a41-3120-b7d3-a7d8e1de8541 | -13.41645 | -47.37865 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f39b19d-c5e0-3ccc-8d57-120224601d4a | -15.15858 | -47.22638 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4c69b95-cd80-38cb-b49f-f12a2bc7c14b | -12.06202 | -45.71606 | 2025-10-29 04:46:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ef86bf2-e38c-38f0-807b-40866d703bee | -9.22859 | -46.34613 | 2025-10-29 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fa6154f0-9543-309d-8079-417eb517e9fa | -14.73177 | -48.16845 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 762ef4df-2729-3560-92c8-ee6a9fb8a467 | -10.38522 | -47.11438 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47c9cf4f-3fc3-3fce-bc8d-8ba416cdc0ce | -11.70074 | -46.70254 | 2025-10-29 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9475d03c-717c-3849-9771-647a51c2a7f2 | -13.17038 | -48.44913 | 2025-10-29 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ce45c4b0-aec6-303d-8abd-1284b9135536 | -10.86432 | -50.09414 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 9dd52d1c-d2b4-34f0-8c23-561f556adbd7 | -10.44163 | -44.70343 | 2025-10-29 04:46:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a66f9589-6fef-381b-ae41-dc61e6369f5e | -10.61351 | -49.61813 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eaa6b976-521e-3c34-a00d-546970d84a53 | -9.79428 | -47.83725 | 2025-10-29 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba804e10-9957-3389-83af-41b5ff2e67fd | -9.51156 | -46.5157 | 2025-10-29 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f885c6d5-6a6f-313d-acd9-ee986fb4c01d | -15.1571 | -47.22784 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f47b7378-983e-3612-b445-905eed841839 | -14.7375 | -48.18508 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 798567ad-f92a-3083-9d2a-7283572f0066 | -10.94026 | -47.62769 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55cef0a3-0551-3d39-8845-b553e69e7b63 | -15.11116 | -43.26506 | 2025-10-29 04:46:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5ef33314-dd51-3714-830f-75ed9d8e8839 | -10.95245 | -47.62487 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 006b0f71-0f79-34a3-8e72-f8e0dadf35b3 | -10.6253 | -47.88537 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a75ddf3a-1f75-3652-8adb-5cd6c4b0e9d3 | -13.21391 | -47.06968 | 2025-10-29 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0c2a2049-c55a-30b1-9461-34abd032d168 | -14.66172 | -50.1857 | 2025-10-29 04:46:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| df38444a-e0aa-3924-a9b4-6ea18e9a0750 | -13.63785 | -46.49251 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b8d5398b-ab35-3457-a59f-a14d12899a9c | -13.55823 | -47.15272 | 2025-10-29 04:46:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a15d90b7-a1a8-3df7-959e-234572b33940 | -13.9556 | -48.46299 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 564fa51f-3c35-320c-a116-f55a0c32919a | -13.23892 | -47.06227 | 2025-10-29 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 317fc757-1343-3df4-8cc6-fe40e9cd7096 | -13.01772 | -48.76795 | 2025-10-29 04:46:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ef97df1c-ddac-3474-88cb-f63a18b0ed32 | -12.36299 | -44.06511 | 2025-10-29 04:46:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8f74ad2-e0b7-3c54-9aaa-1dfc331f28aa | -8.72467 | -49.77152 | 2025-10-29 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 423f0b0c-5714-3515-abaa-bfee83183798 | -14.75089 | -49.66693 | 2025-10-29 04:46:00 | NOAA-20 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 51a59fe3-aa10-316a-9f34-5ba62f1e52fe | -13.35648 | -47.38948 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82bde242-13e9-3777-b63a-a23c6fa7fa26 | -13.67094 | -47.17878 | 2025-10-29 04:46:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8e53d21-249b-33f6-a948-359f0f388f0d | -10.57984 | -49.75541 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f36e8b3-dd78-3da3-938b-d6868a2edc4a | -15.3204 | -47.85922 | 2025-10-29 04:46:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43f0cffc-b72e-33de-8722-87c0d1d80472 | -13.23301 | -47.99606 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 1dd0b8c4-cc8c-3c76-8311-d77cb8a7afb5 | -10.2303 | -52.15154 | 2025-10-29 04:46:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 968c37b1-e283-3aaf-9085-fc89a7d4457a | -10.44067 | -44.70034 | 2025-10-29 04:46:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4ae3899-eb0a-355d-834f-2bbae5c6b745 | -13.63675 | -46.48559 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b49fac6b-33e9-3d87-8b3d-088513bebe53 | -13.68945 | -47.66263 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44884658-1501-3562-995c-c139d8b0dbef | -13.53991 | -47.35274 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 81b701fd-4cd7-3836-88ad-4160e71b6e75 | -9.76329 | -47.85889 | 2025-10-29 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d8521438-b9dd-3056-b96b-7086a5ea8372 | -14.61122 | -48.43544 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be1594c8-1a9d-3de6-9cb1-b369b673cff2 | -13.15647 | -47.09176 | 2025-10-29 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb92bf94-262f-3b47-a19b-a28ab97f5b30 | -13.64292 | -47.02345 | 2025-10-29 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8fb6b7e6-331b-3923-a972-2e01e592fed9 | -15.16187 | -47.22412 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59d9fc57-ee3e-32a9-bdda-d293d4dc2cc1 | -13.32493 | -47.44014 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f5d7fd77-916d-34ff-88e6-396e2ccc1107 | -10.86034 | -50.09734 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 273491f2-29f0-382a-a8d8-3ca026285296 | -10.77399 | -45.10727 | 2025-10-29 04:46:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61669428-9bc9-3852-9972-49fa00526e30 | -14.10241 | -50.33247 | 2025-10-29 04:46:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22f2096f-e3d3-356c-b370-89a621d4a273 | -12.38917 | -50.16701 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a6a1db11-72d9-31c5-9e0c-148cf41849f4 | -10.5764 | -49.75488 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7557a15d-9f26-38f0-ac6a-84b4a3d47f3f | -12.10257 | -47.15686 | 2025-10-29 04:46:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35888e9d-218d-32ca-bf10-fcbaab27fe72 | -11.02675 | -44.65052 | 2025-10-29 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 189ae252-a76a-359f-ba64-9a51cc4b9f14 | -15.79285 | -45.19653 | 2025-10-29 04:46:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2d19e71-fb4d-3799-9eb4-b9b15ad2f7a2 | -13.56193 | -47.15638 | 2025-10-29 04:46:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3b4e339-f7ff-3335-91ff-6768be201143 | -13.64052 | -46.4903 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d5f9845-77e8-3c30-9b24-53f3ad0aaf4c | -11.3708 | -47.01867 | 2025-10-29 04:46:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6705b6f2-8205-3bf6-9e6f-c82d0c98695a | -13.91374 | -48.46128 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8b791b79-2761-3c19-8527-3cb2d7eb3cbc | -12.15574 | -47.6891 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 38a2c081-99b8-35e2-8d92-e093a05a0dd9 | -14.60371 | -48.40443 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c29378d-58fd-37c2-8ee8-d7b6bb0655b2 | -11.58849 | -47.95601 | 2025-10-29 04:46:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 98c95088-280d-376f-8ee1-39f9f0ea6a76 | -11.26132 | -47.81453 | 2025-10-29 04:46:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b1b6b37-5f89-3ef1-9b4e-9f42b999253c | -14.62037 | -45.00185 | 2025-10-29 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cbb11f35-60b9-3156-800f-9065775c966e | -13.89551 | -48.50722 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README74.md)

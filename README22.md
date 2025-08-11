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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ee11eba-0188-32de-a899-2f02214bcc90 | -7.02085 | -55.41775 | 2025-08-11 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 197d502f-376e-3b1e-9293-e9ca5b796026 | -7.06079 | -59.20763 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25a5eb10-5bc7-3dc9-8c72-de5f1899e189 | -10.37135 | -50.83368 | 2025-08-11 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b9bc1fd-18b8-3870-9037-cce8a01080c5 | -8.92899 | -60.75539 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f935989-6a2e-3171-930f-bfaa30d56952 | -9.37195 | -61.53498 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8af38b53-eb6a-34b3-81c5-653262656a90 | -7.05526 | -59.19967 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c08992d0-98d7-38c7-b4b0-bc99f8fd6a5b | -7.07449 | -59.18496 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c06dcfe-dfc5-307e-9f04-bcf9b39b6251 | -7.08387 | -59.18998 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2058ee9a-5c9f-380d-af05-ee4281d397b3 | -11.71497 | -50.10958 | 2025-08-11 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3fa95b3-16c3-3e1d-8475-8a275fa16067 | -11.69336 | -50.1271 | 2025-08-11 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 337989e6-364a-38c3-af53-756f2e83789a | -12.60945 | -47.13356 | 2025-08-11 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b8514f3-a75c-311e-bcde-1ccf3b69be2a | -11.69287 | -50.13104 | 2025-08-11 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a07b7884-4f01-3e9e-b757-b45fc409cda1 | -5.88692 | -57.74723 | 2025-08-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42adf6a6-a4c6-3fb2-989f-235d30d61651 | -8.7961 | -52.06292 | 2025-08-11 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 25a5cb8c-1e9a-3165-b991-deb0e951a64a | -8.93347 | -60.74881 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2609ac5e-7523-3b61-ac18-1642bcdf9174 | -8.93851 | -60.73869 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4054e4fa-c413-303c-9f14-5f6f8030f93e | -8.90836 | -60.54527 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59cd7a81-b17c-31c6-9fa9-ca65f3c84089 | -8.56571 | -54.67777 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78441171-9128-3606-bfa4-ad0dda783b70 | -7.07834 | -59.18203 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95b58c0a-56c2-3110-8dc6-0e693ea09494 | -8.93297 | -60.73053 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 502b15bd-9d7d-3a3f-bdf3-4f0b0fbaa6b8 | -12.54587 | -47.07338 | 2025-08-11 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fd533c1f-7717-36fb-9563-1e577f0c34c0 | -8.57123 | -54.69658 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b20f4fe0-e01e-3bdc-9718-0584306f23a4 | -7.06788 | -59.18393 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57955b2a-b8eb-3d2a-b9a7-d98f517b4ed1 | -9.37774 | -61.52078 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04e227dd-f5b8-3c70-bb0b-67109471af07 | -8.92584 | -60.7585 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8485c5bf-2f8d-3cd6-b061-0a2d4dbf8986 | -7.0784 | -59.20329 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 715c1bbb-671c-3961-9b8f-707221b2992d | -11.75433 | -51.62132 | 2025-08-11 05:18:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73e5b208-fe9f-3bc2-bac7-81a49254a49a | -9.37035 | -61.52337 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76b06456-ddab-30a6-a196-66cad5026e8d | -6.10424 | -59.92726 | 2025-08-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7365148e-d06b-349b-b8ea-73c03921ce7c | -9.37934 | -61.53239 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| efc9a591-ddc1-35c2-aa00-d8fb4e691d62 | -7.0662 | -59.17304 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c178a36b-02a2-3d15-a95b-43ebce92e8d9 | -8.93958 | -60.75344 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e993ae1-4d6a-3f36-81c2-c03a02b4c6b5 | -11.78317 | -49.56772 | 2025-08-11 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 17f2ef13-4b43-3315-9bbb-9a8c3c971434 | -8.1334 | -47.42886 | 2025-08-11 05:18:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| d425865a-ea59-388e-baef-820c7885b29d | -7.07125 | -59.20571 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f228c8c2-76a3-366a-b11f-b7d1a32f0da3 | -7.05297 | -59.17097 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d3ca854-d6df-303b-b188-f284d8e280e8 | -8.93184 | -60.73763 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f7481e5d-43e3-33e4-8834-88e270cc3bee | -7.06842 | -59.18047 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3e2cff5-73da-375a-bca9-4545c7fa088d | -8.93631 | -60.73106 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| dfa2b3b2-ba4e-30ec-bad6-9abbc9cc6d2d | -7.08556 | -59.20086 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9788d06-9508-35f5-a919-99d5118f1fd6 | -9.38053 | -61.52502 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 42fc793b-6ddc-36b5-95b7-e721228b2955 | -12.60785 | -47.15017 | 2025-08-11 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af86c545-c9c2-3a61-bf3a-35159ce132ec | -12.55344 | -47.06819 | 2025-08-11 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0991ae36-cf08-3773-acd7-a19afdc98f0f | -8.57672 | -54.6866 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46cbc9b3-c765-385f-8e97-10dbcff9d8fa | -11.27627 | -50.19373 | 2025-08-11 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0be92f13-7d6b-3e48-b002-9eabc5569beb | -9.37994 | -61.52871 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 52a5fd3e-2172-3fcb-9461-e98946fffa2d | -8.927 | -60.72953 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f28a8307-1b0a-3bd0-af34-da70cd1d0fcb | -11.78365 | -49.56355 | 2025-08-11 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 131e69c8-39c8-3124-af55-391e1d46af69 | -7.06404 | -59.18687 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8f2fe4c-f773-3c3e-be78-313e97f4d04e | -9.37654 | -61.52816 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d9ce9ea3-263f-3896-b48e-d37c4cc6be55 | -8.93681 | -60.74934 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30675a58-6422-31fc-9491-57107ea52f24 | -8.56673 | -54.69946 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 04947dbc-7ebe-3c76-bcf4-aceeb44d377a | -7.0641 | -59.20814 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 09d68c3a-37b0-347e-8333-becee1bbe6cc | -7.07166 | -59.15973 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2769f700-271e-3a49-bffe-e96c243f2208 | -7.06896 | -59.17702 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9f26bd8-8703-3962-bb8c-879297912bb9 | -9.38453 | -61.52188 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 384e0b76-8e0f-3d7b-a073-8094eb7c57b5 | -7.06572 | -59.19777 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6fbefcd7-18a7-3755-a18e-cc81f6a75cba | -7.05803 | -59.20365 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8bd6c56-f7f0-39c1-ac01-c5355d57efcd | -9.19759 | -59.67897 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19e4b61b-5566-3fa2-9f32-5ca5dbe62aff | -5.89028 | -57.74773 | 2025-08-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f78924b-b901-3526-9868-5b8e48c0334a | -7.06741 | -59.20866 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a63ea7c6-f50e-3e6c-8978-c837f465e8fd | -10.36685 | -50.82627 | 2025-08-11 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0107e2df-564d-3542-ad0c-afa1e2f94209 | -7.07119 | -59.18445 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f636fafb-cae2-3480-876d-39b9f0573a8b | -8.94017 | -62.22093 | 2025-08-11 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b4a8e0e-33d1-31d7-9bbf-69b9d4073da0 | -11.76536 | -49.11728 | 2025-08-11 05:18:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60023899-1ebe-3e31-9382-a96177cb1df8 | -5.88973 | -57.75131 | 2025-08-11 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b8437ef0-9524-3b34-bfdf-5e991debf687 | -8.57372 | -54.67893 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cabb3512-f0b6-3935-8fd8-a20ceb57f451 | -12.60985 | -47.13102 | 2025-08-11 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d952821-2271-3a83-8ac0-f24c83dd8df1 | -7.07071 | -59.20918 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ea4b81b3-6457-3846-bb95-0078e67f21d1 | -8.57322 | -54.68247 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fc09c7c-9e5b-34d1-883b-3d8b2787d7f9 | -7.06957 | -59.19482 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2ff152f-6c91-3a70-8fa0-2f0c8d733d99 | -12.60852 | -47.14374 | 2025-08-11 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b668104-b3f9-375f-a208-14a7eb09c6bf | -7.05965 | -59.19328 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 391ecdde-dbd6-3074-be27-00b93d027d96 | -7.25356 | -59.99525 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a2de1a6-2c09-3d58-b83a-653771f5b700 | -7.08165 | -59.18254 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7cf715e-e351-39be-8587-6a3336d2493d | -9.92581 | -60.47849 | 2025-08-11 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 803b4b86-777e-32e6-a311-b4d249bc8ac7 | -6.09758 | -59.92623 | 2025-08-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ffe9281-0c0e-3049-ae34-149f67379c0e | -11.71543 | -50.10561 | 2025-08-11 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c97e0e6f-7149-3d7b-95d6-9b3f9ed56473 | -9.38113 | -61.52134 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49f018cc-fcc3-3703-a95c-f60a4f0e01fd | -7.07402 | -59.20969 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7e21657b-0371-3e5d-9899-15e5b68f7df4 | -8.56974 | -54.70706 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5d929b3e-ce89-3c9c-96d7-0b24c807b26c | -8.57622 | -54.69012 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92e2f87c-afbf-3543-966a-497b9dc0fef2 | -8.56624 | -54.70295 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0db7b13f-2063-3484-8b79-d450509d457e | -7.06782 | -59.16267 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d9f3dd6-3723-3b6e-86fe-dd25b71d6134 | -11.26548 | -50.18835 | 2025-08-11 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f481d697-df88-353d-af9d-250a12ae2271 | -8.13446 | -47.43055 | 2025-08-11 05:18:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 3752526f-990b-3b6f-be92-27f8a0f89755 | -8.56872 | -54.68542 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f60b7e8-c243-337f-9ff0-b31575dc5e5e | -7.05574 | -59.17495 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e3106d1-6a80-3e05-8f55-9a1a64b660a9 | -7.09379 | -59.19152 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21287bfb-4911-3a60-aafe-38b0abf7e2d1 | -11.77726 | -49.56697 | 2025-08-11 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 52ba98ae-78ab-310c-b8d2-1a5a3e8b6f36 | -8.92956 | -60.75183 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78546fb6-b179-3ec8-b1a5-e703a302ef21 | -7.0558 | -59.19622 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9ac63b6-cc3d-3ab3-8cda-e9336477fafe | -11.76483 | -49.12186 | 2025-08-11 05:18:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0bd9d58-8904-3469-89c1-295fb272e01d | -8.93624 | -60.7529 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c201e8b-0a51-3c68-a1df-f795aa433839 | -7.07895 | -59.19983 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 08cd30f0-23df-38a5-9043-516f480bbdff | -7.05857 | -59.20019 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c49b51d1-ef7c-3913-b009-45744b3ec871 | -7.06464 | -59.20468 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 22c38e3c-16c6-3bed-ade5-33370bc23fbe | -7.05749 | -59.2071 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6dd1669c-587d-342a-aa57-ec36d3529a31 | -7.07503 | -59.18151 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f314ded9-bd4b-3771-9579-b9b03884dba7 | -7.40554 | -60.00188 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README23.md)
